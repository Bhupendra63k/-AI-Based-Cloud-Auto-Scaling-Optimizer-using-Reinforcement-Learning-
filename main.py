from fastapi import FastAPI
from pydantic import BaseModel
from env import CloudEnv

app = FastAPI()

env = CloudEnv()

class ActionInput(BaseModel):
    action: int

@app.post("/reset")
async def reset():
    state = env.reset()
    return {
        "observation": list(state)   # 🔥 FIX HERE
    }

@app.post("/step")
async def step(input: ActionInput):
    state, reward, done, info = env.step(input.action)
    return {
        "observation": list(state),  # 🔥 FIX HERE
        "reward": float(reward),
        "done": bool(done),
        "info": info
    }