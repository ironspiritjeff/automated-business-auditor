from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI(title="Automated Business Auditor")

class SimpleUploadRequest(BaseModel):
    filename: str
    character_count: int

@app.get("/health")
async def check_health():
    return {
        "status": "healthy",
        "service": "Automated Business Auditor",
        "tier": "development"
    }

@app.post("/audit/upload")
async def stage_document(payload: SimpleUploadRequest):
    return {
        "message": f"Document '{payload.filename}' has been safely staged.",
        "processed_characters": payload.character_count,
        "status": "staged"
    }

MOCK_DATABASE = [
    {"filename": "q4_walkthrough.pdf", "character_count": 45000, "status": "completed"},
    {"filename": "travel_policy.pdf", "character_count": 120000, "status": "processing"}
]

@app.get("/audit/documents")
async def list_documents():
    return MOCK_DATABASE

@app.get("/audit/documents/{filename}")
async def get_document(filename: str):
    for doc in MOCK_DATABASE:
        if doc["filename"] == filename:
            return doc
    raise HTTPException(status_code=404, detail="Document not found")


# Endpoint 1 (Health status check): http://127.0.0.1:8000/health
# Endpoint 2 (Staged documents list query): http://127.0.0.1:8000/audit/documents
        # To test: Invoke-RestMethod -Uri "http://127.0.0.1:8000/audit/upload" -Method Get
# Endpoint 3 (Document pipeline upload POST): http://http://127.0.0.1:8000/audit/upload
    # To test: Invoke-RestMethod -Uri "http://127.0.0.1:8000/audit/upload" -Method Post

