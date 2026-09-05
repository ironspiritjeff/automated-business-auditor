FROM python:3.14-slim

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY pyproject.toml uv.lock ./
# 4. Copy your environment lock declarations first to maximize Docker's layer caching speed

RUN uv sync --frozen --no-cache
# 5. Synchronize your virtual environment packages natively inside the container shell

COPY main.py .
# 6. Copy your main application file code layout into the isolated workspace directory

EXPOSE 8000
# 7. Expose the specific network port your server listens to

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# 8. Set the permanent boot command to launch your server via your locked environment context
