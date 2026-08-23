from fastapi import FastAPI
from pydantic import BaseModel

# FastAPI app instance
app = FastAPI(
    title="Automated Business Auditor",
    description="Enterprise-grade compliance orchestration and risk detection platform backend shell",
    version="1.0.0"
)


class SimpleUploadRequest(BaseModel):
    file_name: str
    character_count: int


# GET route for health check
app.get("/health")


async def health_check():
    return {
        "status": "healthy",
        "service": "Automated Business Auditor",
        "tier": "development"
    }


@app.post("/audit/upload")
async def stage_document(payload: SimpleUploadRequest):
    return {
        "message": f"Document '{payload.filename}' staged successfully with {payload.character_count} characters.",
        "processed_characters": payload.character_count,
        "status": "staged"
    }

MOCK_DATABASE = [
    {"filename": "q4_walkthrough.pdf", "character_count": 15000, "status": "completed"},
    {"filename": "training_manual.docx", "character_count": 8000, "status": "completed"}
]

@ app.get("/audit/documents")
async def list_documents():
    return {
        "documents": MOCK_DATABASE,
        "total_documents": len(MOCK_DATABASE)
}
