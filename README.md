## AI Test Plan Management Tool

This project is a lightweight AI-assisted test planning application consisting of a Python FastAPI backend and a simple browser-based frontend. The tool allows uploading requirement documents (PDF or DOCX), extracting content, generating suggested test steps, and creating, viewing, editing, and deleting structured test plans. For this assignment, the application runs entirely on localhost, as the backend requirements specified using Python rather than deploying to a cloud environment. The OpenAI API key is provided directly in the backend file for simplicity and compatibility across different local environments, since no deployment or secrets-management layer was required. Test plans are stored in local in-memory storage, which aligns with the scope of a non-deployed, assignment-level prototype.

---

## How to Run the Application

### Requirements

* Python 3.9+
* Git installed
* OpenAI API key with credits

### Clone and Run

Clone repository
```bash
git clone <the repo>
```
Switch into the project directory
```bash
cd Test_plan_management_tool
```

### Backend Setup

```bash
cd backend
```
Create and activate virtual environment
```bash
python3 -m venv venv
```
For Mac / Linux
```bash
source venv/bin/activate
```         
For  Windows CMD
```bash
.\venv\Scripts\activate            
``` 
Install dependencies
```bash
pip install -r requirements.txt
``` 
**Add your OpenAI API key:**

Edit `backend/ai.py` and replace the PASTE_KEY_HERE on line 6:

```python
OPENAI_API_KEY = "PASTE_KEY_HERE"
```
so that it looks like this
```python
OPENAI_API_KEY = "sk-123456789..."
```
Start the backend server
```bash
uvicorn main:app --reload --port 8000
```

### Frontend Setup
Open a new terminal, 
then switch into the frontend
```bash
cd frontend
```
Start the frontend
```bash
python3 -m http.server 5500
```
Open [http://localhost:5500](http://localhost:5500) in a browser.
The application is fully usable once the backend is running and `http://localhost:5500` is open.

---

## Directions 

1. Setup everything according to the previous instructions
2. Make sure AI mode is set to remote
3. Click on `Choose File` in order to upload a file
4. Click on `Extract Text`
5. Adjust the # of Steps; you can choose anywhere from 1-50
6. Click `Generate Test Steps`
7. Edit the generated plan if you want
8. Click on `Save / Update Plan`

---

## Features

* Upload and extract text from PDF and DOCX
* Automatically generates test plan titles, descriptions, and steps
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

