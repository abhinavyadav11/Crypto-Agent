import os
import sys
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse


# Set up import path for internal modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from LLM.llm_agent3 import CryptoAgentLLM

# Initialize FastAPI app
app = FastAPI(title="CryptoAgent API", version="1.0")
agent = CryptoAgentLLM()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],  # or ["*"] to allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route
@app.get("/")
def read_root():
    return JSONResponse(
        content={"message": "🚀 Welcome to CryptoAgent API! Use /query?q=your-question to ask about crypto."}
    )

# GET endpoint to handle crypto queries
@app.get("/query")
async def query_crypto(q: str = Query(..., min_length=2, max_length=100, description="Your crypto question")):
    try:
        answer = agent.answer_query(q)
        return {"query": q, "answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")
