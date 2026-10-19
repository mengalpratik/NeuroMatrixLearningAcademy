#!/usr/bin/env bash
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"

MODE="${1:-prod}"

echo "=========================================================="
echo "  NEUROMATRIX LEARNING ACADEMY — 112-DAY FULL-STACK RUNNER"
echo "=========================================================="

# Check Python environment
if [ ! -d "backend/.venv" ]; then
    echo "[!] Setting up Python virtual environment with uv..."
    uv venv backend/.venv
    uv pip install --python backend/.venv -e "backend[dev]"
fi

# Check frontend build
if [ ! -d "frontend/dist" ] || [ "$MODE" = "build" ]; then
    echo "[*] Building frontend production bundle..."
    cd frontend
    if [ ! -d "node_modules" ]; then
        npm install
    fi
    npm run build
    cd "$DIR"
fi

if [ "$MODE" = "dev" ]; then
    echo "[*] Starting NeuroMatrix Academy in DEVELOPMENT mode..."
    echo "    Backend API: http://127.0.0.1:8000"
    echo "    Frontend Dev: http://127.0.0.1:5173"
    
    # Run backend in background and frontend in foreground
    backend/.venv/bin/uvicorn app.main:app --app-dir backend --host 127.0.0.1 --port 8000 --reload &
    BACKEND_PID=$!
    
    trap "kill $BACKEND_PID 2>/dev/null || true" EXIT
    
    cd frontend
    npm run dev -- --host 127.0.0.1 --port 5173
else
    echo "[*] Starting NeuroMatrix Academy in PRODUCTION mode..."
    echo "    Application URL: http://127.0.0.1:8000"
    echo "    Swagger Docs:    http://127.0.0.1:8000/docs"
    echo "=========================================================="
    exec backend/.venv/bin/uvicorn app.main:app --app-dir backend --host 0.0.0.0 --port 8000
fi
