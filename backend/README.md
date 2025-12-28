# AI SQL Agent Backend

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Set environment variables:
   - `POSTGRES_URL` (e.g. `postgresql://readonly:readonly@localhost:5432/yourdb`)
   - `OPENAI_API_KEY`
   - `OPENROUTER_API_KEY` (get from https://openrouter.ai)
   - (Optional) `OPENROUTER_MODEL` (default: `openrouter/openai/gpt-3.5-turbo`)
3. Run the server:
   ```
   uvicorn backend.main:app --reload
   ```

## API

POST `/query`
- Input: `{ "question": "string" }`
- Output: `{ "sql": "string", "data": [ ... ], "verification": { ... } }`
