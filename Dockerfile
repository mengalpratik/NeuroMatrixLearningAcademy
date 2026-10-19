# ==============================================================================
# NeuroMatrix Learning Academy - Production Multi-Stage Dockerfile
# ==============================================================================

# --- Stage 1: Build Frontend Assets ---
FROM node:20-alpine AS frontend-builder

WORKDIR /app/frontend

COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci

COPY frontend/ ./
RUN npm run build

# --- Stage 2: Production Python Runtime ---
FROM python:3.13-slim AS runtime

# System configuration & environment
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app/backend \
    PATH="/opt/venv/bin:$PATH" \
    PORT=8000 \
    HOST=0.0.0.0 \
    DATABASE_URL="sqlite+aiosqlite:////app/data/neuromatrix_academy.db"

# Install curl for container health check
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# Create dedicated non-root user and directories
RUN groupadd -g 1000 academy \
    && useradd -u 1000 -g academy -s /bin/bash -m academy \
    && mkdir -p /app /app/data /opt/venv \
    && chown -R academy:academy /app /opt/venv

# Install Python virtual environment & dependencies
WORKDIR /app
COPY backend/requirements.txt /app/requirements.txt
RUN python -m venv /opt/venv \
    && /opt/venv/bin/pip install --no-cache-dir --upgrade pip \
    && /opt/venv/bin/pip install --no-cache-dir -r /app/requirements.txt

# Copy backend application source
COPY backend/ /app/backend/

# Copy compiled frontend production assets from Stage 1
COPY --from=frontend-builder /app/frontend/dist /app/frontend/dist

# Secure ownership of all application assets
RUN chown -R academy:academy /app

# Switch to non-root user
USER academy

# Expose internal service port
EXPOSE 8000

# Container healthcheck
HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 \
    CMD curl -f http://127.0.0.1:8000/api/health || exit 1

# Production entrypoint
WORKDIR /app/backend
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
