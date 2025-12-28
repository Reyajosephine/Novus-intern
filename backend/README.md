
# AI SQL Agent Backend

This backend powers the AI SQL Agent system, converting natural language questions into safe, validated SQL queries, executing them on a cloud PostgreSQL database, and verifying the results using an LLM.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Set environment variables:**
   - `POSTGRES_URL` (e.g. `postgresql://readonly:readonly@localhost:5432/yourdb` or Neon cloud URL)
   - `OPENROUTER_API_KEY` (get from https://openrouter.ai)
   - (Optional) `OPENROUTER_MODEL` (default: `openai/gpt-3.5-turbo`)
3. **Run the server:**
   ```bash
   uvicorn backend.main:app --reload
   ```

## API Endpoint

### POST `/query`
- **Input:** `{ "question": "string" }`
- **Output:** `{ "sql": "string", "data": [ ... ], "verification": { "status": str, "confidence": float, "reason": str } }`

## How it Works

1. Loads the live database schema from PostgreSQL (cloud, e.g. Neon)
2. Uses OpenRouter LLM to generate a safe, deterministic SQL SELECT query
3. Validates SQL for safety (read-only, no SELECT *, no modifications)
4. Executes SQL and fetches results
5. Verifies the result using an LLM for correctness and provides a confidence score and explanation

## Tech Stack
- Python 3, FastAPI, SQLAlchemy, Pydantic, Requests
- OpenRouter API (LLM, e.g. GPT-3.5-turbo)
- PostgreSQL (cloud, e.g. Neon)

## Security
- Only allows safe, read-only SQL
- CORS enabled for frontend access
- No stack traces or sensitive info in errors

## Example

Request:
```json
{
  "question": "Show all customers who purchased a laptop."
}
```
Response:
```json
{
  "sql": "SELECT ...",
  "data": [ ... ],
  "verification": {
    "status": "valid",
    "confidence": 0.95,
    "reason": "The results match the question."
  }
}
```
