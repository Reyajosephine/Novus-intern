# AI SQL Agent Backend

## Setup

1. Install dependencies:
   ```
pip install -r requirements.txt
   ```
2. Set environment variables:
   - `POSTGRES_URL` (e.g. `postgresql://readonly:readonly@localhost:5432/yourdb`)
   - `OPENAI_API_KEY`
3. Run the server:
   ```
uvicorn main:app --reload
   ```

## API

POST `/query`
- Input: `{ "question": "string" }`
- Output: `{ "sql": "string", "data": [ ... ], "verification": { ... } }`
