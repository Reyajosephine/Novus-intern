
# AI SQL Agent Frontend

This is the web dashboard for the AI SQL Agent system. It allows users to enter natural language questions, view generated SQL, see results, and get verification feedback—all in a modern, branded UI.

## Usage

1. Open `index.html` in your browser (or serve via a static file server).
2. Ensure the backend FastAPI server is running at `http://localhost:8000` (default).
3. Enter a natural language question and click **Run Query**.

## Features
- Modern, responsive dashboard UI (Novus Solutions branding)
- Query input, SQL display, results table, and verification panel
- Real-time feedback: loading spinner, error badges, confidence scores
- Secure: only works with backend API (no direct DB access)

## File Structure
- `index.html` – Main dashboard UI
- `style.css` – Responsive, branded styles
- `app.js` – Handles API calls, rendering, and user interaction
- `assets/Novus-logo.png` – Novus Solutions logo

## Notes
- For production, serve via a proper static file server and secure backend API access (CORS enabled).
- All data is fetched from the backend; no direct DB or LLM calls from the frontend.
