# Automated Business Auditor 🚀

An enterprise-grade, asynchronous backend pipeline engine designed to evaluate corporate records, extract document telemetry, and run autonomous risk compliance audits using generative AI models. This repository serves as a core portfolio asset demonstrating clean application-layer AI engineering, structured environment isolation, and micro-service containerization.

## 🛠️ Technical Architecture

- **Runtime Environment:** Python 3.14 (Optimized Workspace Dependency Locking via `uv`)
- **Web Framework:** FastAPI (Asynchronous ASGI server layer)
- **Containerization:** Docker Multi-Stage Builds (`python:3.14-slim` base image)
- **Dependency Management:** `uv` (`pyproject.toml` workspace environment)
## 📡 Active Core Infrastructure

- **Global Telemetry Middleware:** Transparent request-response stopwatch logging pipeline processing speeds natively to stdout.
- **Data Valuation Layers:** Pydantic v2 schemas validating incoming document metadata packages and multi-dimensional JSON input envelopes.
- **Container Interface:** Port forwarding configurations (`-p 8000:8000`) ready for horizontal cloud routing layers (Render/AWS).
## 🚀 Local Deployment Setup

Ensure you have `uv` and Docker Desktop installed on your host machine.
### 1. Native Workspace Sync
```powershell
uv sync --frozen
uv run uvicorn main:app --reload
```
### 2. Standalone Container Compilation
```powershell
docker build -t ironspiritjeff/automated-auditor:1.0.0 .
docker run -d -p 8000:8000 --name active-auditor ironspiritjeff/automated-auditor:1.0.0
```
## ⏱️ Interactive Routing Verification
```powershell
# 1. Structural Heartbeat Check
Invoke-RestMethod -Uri "http://127.0.0" -Method Get
# 2. Document Parsing Telemetry Check
\$DataPackage = @{ filename = "corporate_records.pdf"; character_count = 210000 } | ConvertTo-Json
Invoke-RestMethod -Uri "http://127.0.0" -Method Post -Body \$DataPackage -ContentType "application/json"
```
**Note** the above links are incomplete


## 📈 Roadmap & Upcoming Iterations
- [x] Establish isolated Python 3.14 FastAPI core skeleton
- [x] Configure request latency tracking telemetry middleware
- [x] Multi-layer containerization build pipeline using `uv`
- [ ] Connect OpenAI API live client orchestration layers
- [ ] Integrate streaming token context calculation modules (`tiktoken`)
- [ ] Implement Model Context Protocol (MCP) tool schema routing contracts
- [ ] Automated continuous integration webhook deployment to Render