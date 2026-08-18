# GitHub Copilot Rules for Automated Business Auditor

## Core Technology Stack
- Framework: FastAPI (Asynchronous Python ASGI backend framework)
- Validation: Pydantic v2 (Enforce strict type validation and explicit Field constraints)
- Database Layer: Neon Serverless Postgres via SQLModel
- AI Architecture: Model Context Protocol (MCP) using fastapi-mcp / fastmcp

## Coding & Architecture Rules
- Use clear, descriptive variable and function names.
- Prefer asynchronous def syntax (`async def`) for all incoming API routes.
- Implement explicit error handling with FastAPI's `HTTPException` and return clean JSON payloads.
- Always include a production-ready `GET /health` monitoring endpoint.
- Structure endpoints using `APIRouter` to keep code clean and modular.

## Quality Standards
- Keep generated code completely production-ready and strongly typed.
- Never write placeholder code or `TODO` markers in functional execution paths.
- Write docstrings for all custom classes and endpoint route handlers.
