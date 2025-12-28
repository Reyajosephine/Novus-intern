from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import os
import requests
import time

# --- CONFIG ---
POSTGRES_URL = os.getenv("POSTGRES_URL", "postgresql://readonly:readonly@localhost:5432/yourdb")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "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")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "openrouter/openai/gpt-3.5-turbo")

# --- FASTAPI APP ---
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- SQLALCHEMY ENGINE ---
engine = create_engine(POSTGRES_URL, pool_pre_ping=True)

# --- Pydantic Models ---
class QueryRequest(BaseModel):
    question: str

class VerificationResult(BaseModel):
    status: str  # valid | warning | invalid
    confidence: float
    reason: str

class QueryResponse(BaseModel):
    sql: str
    data: list
    verification: VerificationResult

# --- SYSTEM PROMPTS ---
SQL_GEN_PROMPT = """
You are a SQL expert. Given the following database schema, generate a safe, deterministic, and correct SQL SELECT query (no SELECT *, no modifications, always LIMIT 100) for the user's question. Use only the provided schema. Output only the SQL.
Schema:
{schema}
Question: {question}
"""

SQL_VALIDATION_PROMPT = """
You are a SQL safety validator. Given this SQL query, does it violate any of these rules: no modifications, no SELECT *, no subqueries without WHERE, only use provided schema? Output 'valid', 'warning', or 'invalid' and a short reason.
SQL: {sql}
"""

DATA_VERIFICATION_PROMPT = """
You are a data verification agent. Given the SQL, the user's question, and the result rows, analyze if the data answers the question, check for anomalies, and explain your reasoning. Output status (valid/warning/invalid), confidence (0-1), and a clear explanation.
Question: {question}
SQL: {sql}
Rows: {rows}
"""

# --- SCHEMA LOADER ---
def load_schema():
    inspector = engine.inspect(engine)
    schema = ""
    for table in inspector.get_table_names():
        schema += f"Table: {table}\n"
        for col in inspector.get_columns(table):
            schema += f"  - {col['name']} ({col['type']})\n"
    return schema

# --- AI AGENT HELPERS ---
def call_openai(prompt, temperature=0):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": OPENROUTER_MODEL,
        "messages": [
            {"role": "system", "content": prompt}
        ],
        "temperature": temperature,
        "max_tokens": 512
    }
    resp = requests.post(url, headers=headers, json=payload, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"].strip()

# --- SQL SAFETY CHECK ---
def is_sql_safe(sql):
    unsafe = ["insert", "update", "delete", "drop", "alter", "select *"]
    for word in unsafe:
        if word in sql.lower():
            return False
    return True

# --- MAIN ENDPOINT ---
@app.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):
    schema = load_schema()
    # Step 1: NL → SQL
    sql_prompt = SQL_GEN_PROMPT.format(schema=schema, question=request.question)
    sql = call_openai(sql_prompt)
    # Step 2: SQL Safety
    if not is_sql_safe(sql):
        raise HTTPException(status_code=400, detail="Unsafe or invalid SQL generated.")
    # Step 3: SQL Validation Agent
    val_prompt = SQL_VALIDATION_PROMPT.format(sql=sql)
    val_result = call_openai(val_prompt)
    if "invalid" in val_result.lower():
        raise HTTPException(status_code=400, detail="SQL validation failed: " + val_result)
    # Step 4: Execute SQL
    try:
        with engine.connect() as conn:
            start = time.time()
            result = conn.execute(text(sql))
            rows = [dict(r) for r in result]
            if time.time() - start > 5:
                raise HTTPException(status_code=408, detail="Query timeout.")
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail="SQL execution error.")
    # Step 5: Data Verification
    ver_prompt = DATA_VERIFICATION_PROMPT.format(question=request.question, sql=sql, rows=rows[:5])
    ver_response = call_openai(ver_prompt)
    # Parse verification (simple parse)
    status, confidence, reason = "warning", 0.5, ver_response
    if "valid" in ver_response.lower():
        status = "valid"
        confidence = 0.95
    elif "invalid" in ver_response.lower():
        status = "invalid"
        confidence = 0.1
    return QueryResponse(
        sql=sql,
        data=rows,
        verification=VerificationResult(status=status, confidence=confidence, reason=reason)
    )
