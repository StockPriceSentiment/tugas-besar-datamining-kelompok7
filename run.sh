#!/bin/bash

# File: run.sh
# Deskripsi: Menjalankan pipeline main.py

echo "Aktifkan environment..."
source .venv/Scripts/activate

echo "Menjalankan pipeline..."
python src/main.py
