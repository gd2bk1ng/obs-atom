#!/usr/bin/env bash
set -e

echo "👑 OBS-Atom Local Dev Environment Setup"

# Step 1: System packages
echo "[INFO] Installing Python toolchain and build essentials..."
sudo apt update
sudo apt install -y python3-full python3-dev python3-venv python3-pip build-essential

# Step 2: Create local venv if not already present
if [ ! -d ".venv" ]; then
    echo "[INFO] Creating virtual environment..."
    python3 -m venv .venv
else
    echo "[INFO] Virtual environment already exists, reusing..."
fi

# Step 3: Activate venv
echo "[INFO] Activating virtual environment..."
source .venv/bin/activate

# Step 4: Upgrade pip/setuptools/wheel
echo "[INFO] Upgrading pip, setuptools, and wheel..."
pip install --upgrade pip setuptools wheel

# Step 5: Install dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo "[INFO] Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "[WARN] No requirements.txt found. Skipping dependency install."
fi

echo "✅ Local dev environment ready! Use 'source .venv/bin/activate' to re-enter later."

