# 🤖 AI SQL Agent

An AI-powered SQL agent that enables users to query databases using **natural language**, automatically generating **safe, verified SQL queries** and returning trusted results through a modern web dashboard.

---

## 📄 Project Report

### Abstract
This project delivers a production-ready **AI-powered SQL agent system** that allows users to ask natural language questions and receive **verified, safe SQL queries and results** from a real database. The system is designed for business users and analysts who want to interact with data securely and intuitively, without writing SQL themselves. The solution features a modern, branded web dashboard and a robust backend pipeline for query generation, validation, execution, and verification.

---

## 🏗️ Architecture

### Frontend (HTML / CSS / JavaScript)
- Responsive dashboard UI
- Query input, generated SQL display, results table, verification panel
- Novus Solutions branding with modern card-based layout
- Communicates with backend via REST APIs

### Backend (FastAPI, Python)
- REST API endpoint: `/query`
- AI agent processing pipeline:
  1. Load database schema
  2. Generate SQL from natural language using OpenRouter (LLM)
  3. Validate SQL for safety and schema compliance
  4. Execute SQL in a read-only environment
  5. Verify results and generate a human-readable explanation
- Security features:
  - Read-only database credentials
  - SQL allow-listing (SELECT-only)
  - Query execution timeouts
  - No internal stack traces exposed to users

### Database (Cloud PostgreSQL – Neon)
- Database type: **PostgreSQL**
- Cloud provider: **Neon (Serverless PostgreSQL)**
- Dataset includes:
  - Customers
  - Products
  - Purchases
- Fully cloud-hosted using Neon’s managed PostgreSQL infrastructure
- No local database setup required
- Read-only access ensures secure query execution

Neon provides a scalable, serverless PostgreSQL environment that is well-suited for cloud-native and AI-driven applications.

![HACK-A-CLOUD](https://github.com/user-attachments/assets/04977372-80a0-4721-b660-eaa98ca081fb)



---

## 🧰 Tech Stack

- **Frontend:** HTML5, CSS3 (Flexbox / Grid), Vanilla JavaScript
- **Backend:** Python 3, FastAPI, SQLAlchemy, Pydantic, Requests
- **AI / LLM:** OpenRouter API (e.g., GPT-3.5-Turbo)
- **Database:** PostgreSQL (Neon – serverless cloud PostgreSQL)
- **Other:** REST APIs, CORS handling, responsive UI design

---

## 🚀 How It Works

1. User enters a natural language question  
   *(e.g., “Show all products with price greater than 1000”)*
2. Backend AI agent:
   - Converts the question into SQL
   - Validates query safety and schema alignment
3. SQL is executed against a **read-only Neon PostgreSQL database**
4. The system returns:
   - Generated SQL query
   - Query results in tabular format
   - Verification status, confidence score, and explanation

---

## 📊 Output

- Generated SQL query displayed to the user
- Query results rendered in a table
- Verification panel showing:
  - Status (valid / warning / invalid)
  - Confidence score
  - Human-readable explanation

**Example 1:**  
Input → *“Total sales count”*  
Output → SQL query, numerical result, and verification summary shown instantly.

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/d22bebb8-5a34-4927-8327-2dd42bc05aae" />
<img width="1919" height="358" alt="image" src="https://github.com/user-attachments/assets/b4b5319a-3a6f-4d03-8aef-8b22c5a4a72d" />



**Example 1:**  
Input → *“List all products”*  
Output → SQL query, numerical result, and verification summary shown instantly.

<img width="1919" height="1090" alt="image" src="https://github.com/user-attachments/assets/d9c9849d-184f-42d8-9c9c-ee1601435580" />
<img width="1919" height="409" alt="image" src="https://github.com/user-attachments/assets/b9f9699a-396c-49a3-a773-a86df2346b6f" />



---

## ⚠️ Challenges Faced

- Ensuring LLM-generated SQL is safe and schema-compliant
- Prompt engineering for reliable SQL generation
- Handling SQL aliasing and edge cases
- CORS and cross-origin communication issues
- Secure cloud database configuration (Neon)
- UI/UX consistency across branding and themes
- End-to-end error handling (LLM, SQL, API, frontend)

---

## 🔮 Future Scope & Enhancements

- Support for additional databases (MySQL, SQLite, MongoDB)
- User authentication and query history
- Advanced data verification (outlier detection, anomaly alerts)
- Customizable prompt templates
- Multi-language natural language support
- Real-time collaboration and sharing
- Export results to CSV / Excel
- Voice input and accessibility enhancements

## 📁 Project Structure

```
NOVUS-INTERN/
├── backend/
│   ├── __pycache__/
│   ├── init_db.sql
│   ├── init_db.sqlite.sql
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
│
├── frontend/
│   ├── assets/
│   │   └── Novus-logo.png
│   ├── app.js
│   ├── index.html
│   ├── style.css
│   └── README.md
│
└── README.md
```

---

## 📦 Folder Overview

### `backend/`
Contains the FastAPI-based AI SQL Agent backend.
- `main.py` – API entry point and query pipeline
- `init_db.sql` – PostgreSQL schema initialization
- `init_db.sqlite.sql` – SQLite schema (optional/local testing)
- `requirements.txt` – Backend dependencies
- `README.md` – Backend setup and API documentation

### `frontend/`
Contains the web-based dashboard UI.
- `index.html` – Main UI layout
- `style.css` – Styling and branding
- `app.js` – Frontend logic and API calls
- `assets/` – Static assets (logos, images)
- `README.md` – Frontend usage instructions

### Root `README.md`
- Project overview
- Architecture
- Tech stack
- Setup instructions
- Future scope

---

## ✅ Notes
- Backend and frontend are **fully decoupled**
- Cloud PostgreSQL is hosted on **Neon**
- Backend exposes REST APIs consumed by the frontend
- Suitable for local development and cloud deployment

---


## ✅ Conclusion

The AI SQL Agent demonstrates a **secure, user-friendly, and production-ready approach** to natural language database querying. By combining AI-driven SQL generation with strict validation and a clean, modern UI, the system empowers users to access insights without technical barriers. Its modular architecture and use of **Neon cloud PostgreSQL** make it scalable and extensible for future enterprise and research use cases.

---
