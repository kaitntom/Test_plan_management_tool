## AI Test Plan Management Tool

This project is a lightweight AI-assisted test planning application consisting of a Python FastAPI backend and a simple browser-based frontend. The tool allows uploading requirement documents (PDF or DOCX), extracting content, generating suggested test steps, and creating, viewing, editing, and deleting structured test plans.

---

## How to Run the Application

### Requirements

* Python 3.9+
* Git installed
* OpenAI API key (only needed for AI generation mode)

### Clone and Run

```bash
# Clone repository
git clone <YOUR_REPO_URL>
cd Test_plan_management_tool
```

### Backend Setup

```bash
cd backend

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate          # Mac / Linux
# OR
venv\Scripts\activate             # Windows

# Install dependencies
pip install -r requirements.txt

# Add your OpenAI key
# Open file: ai.py
# Replace the first PASTE_KEY_HERE
```

```bash
# Start API server
uvicorn main:app --reload --port 8000
```

### Frontend Setup

```bash
cd ../frontend
python3 -m http.server 5500
# Open http://localhost:5500 in a browser (double-click or open with Live Server)
```

The application is fully usable once the backend is running and `http://localhost:5500` is open.

---

## Features

* Upload and extract text from PDF and DOCX
* AI-generated test plan title, description, and steps
* Manual editing of all fields including individual steps
* Create, edit, delete, and manage multiple saved plans
* No build steps required, runs locally in minutes

---

## Architecture Summary

| Layer         | Technology        | Purpose                                        |
| ------------- | ----------------- | ---------------------------------------------- |
| Backend API   | FastAPI (Python)  | REST endpoints, AI calls, file extraction      |
| AI logic      | OpenAI API        | Structured test step generation                |
| File parsing  | PyPDF2 + docx2txt | Convert uploaded files to plain text           |
| Data handling | In-memory storage | Lightweight CRUD for assignment scope          |
| Frontend      | HTML + JavaScript | Direct browser-based UI, no framework required |

This approach ensures clarity, small footprint, fast local setup, and easy inspection of all logic.

---

## AI Assistance Citation

Portions of this project were developed with assistance from OpenAI ChatGPT for code structuring, refinement, and documentation formatting. All logic, implementation steps, and decisions were reviewed and understood during development.

