from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time
from engine import get_best_move

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MoveRequest(BaseModel):
    fen: str
    depth: int

@app.post("/api/move")
def move(request: MoveRequest):
    start_time = time.time()
    
    result = get_best_move(request.fen, request.depth)
    
    end_time = time.time()
    
    return {
        "move": result["move"],
        "positions": result["positions"],
        "timeTaken": (end_time - start_time) * 1000 # convert to ms
    }
