#!/bin/bash

# Pull the Mistral model if not already downloaded
ollama pull mistral

# Start Ollama in background
ollama serve &

# Wait for Ollama to boot up
sleep 5

# Start Flask server
python app.py
