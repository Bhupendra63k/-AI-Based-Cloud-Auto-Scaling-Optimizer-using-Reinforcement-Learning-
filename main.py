from fastapi import FastAPI
from pydantic import BaseModel
from env import CloudEnv

app = FastAPI()

env = CloudEnv()

class ActionInput(BaseModel):
    action: int

@app.get("/")
def root():
    return {"message": "Cloud Auto Scaling Env Running"}

@app.post("/reset")
async def reset():
    state = env.reset()
    return {"observation": list(state)}

@app.post("/step")
async def step(input: ActionInput):
    state, reward, done, info = env.step(input.action)
    return {
        "observation": list(state),
        "reward": float(reward),
        "done": bool(done),
        "info": info
    }