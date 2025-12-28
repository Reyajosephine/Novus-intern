# AI SQL Agent – Project Report

## Abstract
This project delivers a production-ready AI-powered SQL agent system that enables users to ask natural language questions and receive verified, safe SQL queries and results from a real database. The system is designed for business users and analysts who want to interact with their data securely and intuitively, without writing SQL themselves. The solution features a modern, branded web dashboard and a robust backend pipeline for query generation, validation, execution, and verification.

## Architecture

**Frontend (HTML/CSS/JS)**
- Responsive dashboard UI
- Query input, SQL/code display, results table, verification panel
- Novus Solutions branding and modern card layout
- Communicates with backend via REST API

**Backend (FastAPI, Python)**
- REST API endpoint `/query`
- AI agent pipeline:
  1. Loads DB schema
  2. Generates SQL from NL using OpenRouter (LLM)
  3. Validates SQL for safety and correctness
  4. Executes SQL (read-only, cloud PostgreSQL)
  5. Verifies data and provides human-readable explanation
- Security: read-only DB, query allow-list, timeout, no stack traces

**Database (Cloud PostgreSQL/Neon)**
- Customer purchase data (customers, products, purchases)
- Hosted in the cloud, no local DB required

## Tech Stack
- **Frontend:** HTML5, CSS3 (Flexbox/Grid), Vanilla JavaScript
- **Backend:** Python 3, FastAPI, SQLAlchemy, Pydantic, Requests
- **AI/LLM:** OpenRouter API (e.g., GPT-3.5-turbo)
- **Database:** PostgreSQL (Neon cloud instance)
- **Other:** Modern CSS, responsive design, CORS, REST

## Output
- Users enter natural language questions (e.g., "Show all products with price > 1000")
- The system displays:
  - The generated SQL query
  - The query results in a table
  - A verification panel with status, confidence, and explanation
  - All sections styled in a modern, branded dashboard
- Example: Ask for "total sales count" → SQL, result, and verification shown instantly

## Challenges Faced
- Ensuring the LLM generates only safe, valid, and schema-compliant SQL
- Handling SQL aliasing and prompt engineering for reliable output
- CORS and cross-origin issues between frontend and backend
- Cloud database setup and connection security
- UI/UX consistency across dark/light themes and branding
- Error handling for all layers (LLM, SQL, API, frontend)

## Future Scope and Enhancements
- Support for more databases (MySQL, SQLite, MongoDB)
- User authentication and query history
- More advanced data verification (outlier detection, anomaly alerts)
- Customizable prompt templates and multi-language support
- Real-time collaboration and sharing
- Export results to CSV/Excel
- Voice input and accessibility features

## Conclusion
This project demonstrates a secure, user-friendly, and production-ready AI SQL agent system. It bridges the gap between natural language and data, empowering users to access insights without technical barriers. The modular architecture and clean UI make it extensible for future business needs and enhancements.
