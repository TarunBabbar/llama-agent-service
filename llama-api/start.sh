#!/bin/bash
set -e  # exit on any error
set -x  # print each command

echo "👉 Pulling Mistral model"
ollama pull mistral

echo "👉 Starting Ollama server"
ollama serve &

echo "⏳ Waiting for Ollama to start..."
sleep 5

echo "🚀 Starting Flask app"
python app.py
