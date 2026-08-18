from fastapi import FastAPI

# initiate an instance of FastAPI called app
app = FastAPI(
    title="Automated Business Auditor API",
    description="Production-grade backend for automated compliance and risk verification.",
    version="0.1.0"
)

# Endpoint 1: Set up the GET skeleton to run a system health check


@app.get("/health", tags=["System"])
def health_check():
    '''This verifies that the server engine and core routes are operational'''
    return {
        "status": "healthy",
        "service": "automated-business-auditor",
        "environment": "development"
    }

# Endpoint 2: Set up the POST skeleton for document uploading


@app.post("/audit/upload", tags=["Auditor Core"])
def check_doc_upload(filename: str, department: str):
    '''This simulates receiving metadata before attaching the AI processing engine'''
    return {
        "message": f"successfully received '{filename}' for auditing.",
        "target_dept": department,
        "status": "staged_for_processing"
    }
