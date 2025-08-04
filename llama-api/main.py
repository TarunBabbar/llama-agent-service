from fastapi import FastAPI, Request
import requests

app = FastAPI()

OLLAMA_BASE = "http://localhost:11434"  # or "http://127.0.0.1:11434" if needed

@app.get("/")
def root():
    return {"message": "Mistral API is live!"}

@app.post("/generate")
async def generate(request: Request):
    body = await request.json()
    prompt = body.get("prompt")

    response = requests.post(
        f"{OLLAMA_BASE}/api/generate",
        json={
            "model": "mistral",   # 👈 changed from "llama3" to "mistral"
            "prompt": prompt
        }
    )
    return response.json()
