from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
import shutil, os
import PyPDF2, docx2txt
from ai import generate_steps


# ---------------- FASTAPI SETUP ----------------

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------- DATA MODELS ----------------

class TestPlan(BaseModel):
    title: str = Field(..., min_length=1)
    description: str = ""
    steps: List[str] = []


class PlanUpdate(BaseModel):
    title: str = Field(..., min_length=1)
    description: str = ""
    steps: List[str] = []


class AIRequest(BaseModel):
    text: str
    max_steps: Optional[int] = 10


# ---------------- STORAGE ----------------

plans = []
next_id = 1



# ---------------- FILE UPLOAD ----------------

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    ext = file.filename.lower().split(".")[-1]
    if ext not in ["pdf", "docx"]:
        raise HTTPException(status_code=400, detail="Only PDF and DOCX allowed")

    tmp_path = f"temp.{ext}"
    with open(tmp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        if ext == "pdf":
            with open(tmp_path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                text = "\n".join([(page.extract_text() or "") for page in reader.pages])
        else:
            text = docx2txt.process(tmp_path)
    finally:
        os.remove(tmp_path)

    return {"text": text}



# ---------------- AI GENERATION ----------------

@app.post("/ai/suggest")
async def ai_suggest(payload: AIRequest):
    if not payload.text.strip():
        raise HTTPException(status_code=400, detail="Input text cannot be empty")

    result = generate_steps(payload.text, payload.max_steps or 10)
    return result



# ---------------- CRUD: PLANS ----------------

@app.get("/plans")
def get_plans():
    return plans


@app.post("/plans")
def create_plan(plan: TestPlan):
    global next_id

    new_plan = plan.dict()
    new_plan["id"] = next_id
    next_id += 1

    plans.append(new_plan)
    return new_plan


@app.put("/plans/{plan_id}")
def update_plan(plan_id: int, plan: PlanUpdate):
    for existing in plans:
        if existing["id"] == plan_id:
            existing["title"] = plan.title
            existing["description"] = plan.description
            existing["steps"] = plan.steps
            return existing
    raise HTTPException(status_code=404, detail="Plan not found")


@app.delete("/plans/{plan_id}")
def delete_plan(plan_id: int):
    global plans
    plans = [p for p in plans if p["id"] != plan_id]
    return {"status": "deleted", "remaining": len(plans)}

