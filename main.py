from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException
import logging
import time
from fastapi import Request

app = FastAPI(title="Automated Business Auditor")

@app.middleware("http")
async def request_latency_log(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time_ms = (time.perf_counter() - start_time) *1000
    print(f"INFO: [TELEMETRY] PATH {request.url.path} | LATENCY {process_time_ms:.2f}ms")
    return response


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("app_logger")


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
    '''
    Validate and stage incoming corporate assets into the data pipeline
    '''
    logger.info(f"Received upload request for file {payload.filename}")

    # Enforce data ingestion constraints: only allow PDF files to be staged
    if not payload.filename.lower().endswith(".pdf"):
        logger.warning(
            f"rejected non-PDF file upload attempt: {payload.filename}")
        raise HTTPException(
            status_code=400, detail="Only PDF files are allowed for upload.")
    return {
        "message": f"Document '{payload.filename}' has been safely staged.",
        "processed_characters": payload.character_count,
        "status": "staged"
    }

MOCK_DATABASE = [
    {"filename": "q4_walkthrough.pdf",
        "character_count": 45000, "status": "completed"},
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


# $BadData = @{ filename = "malicious_report.docx"; character_count = 12000 } | ConvertTo-Json
# Invoke-RestMethod -Uri "http://127.0.0.1:8000/audit/upload" -Method Post -Body $BadData -ContentType "application/json"
