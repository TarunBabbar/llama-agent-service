from fastapi import FastAPI, Request
import requests

app = FastAPI()

OLLAMA_BASE = "http://localhost:11434"  # Default Ollama port

@app.get("/")
def root():
    return {"message": "LLaMA API is live!"}

@app.post("/generate")
async def generate(request: Request):
    body = await request.json()
    prompt = body.get("prompt")

    response = requests.post(
        f"{OLLAMA_BASE}/api/generate",
        json={"model": "llama3", "prompt": prompt}
    )
    return response.json()