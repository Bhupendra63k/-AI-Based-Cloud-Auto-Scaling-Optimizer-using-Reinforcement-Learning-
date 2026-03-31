from fastapi import FastAPI
from pydantic import BaseModel
from env import CloudEnv

app = FastAPI()

env = CloudEnv()

# Request format
class ActionInput(BaseModel):
    action: int

@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state}

@app.post("/step")
def step(input: ActionInput):
    state, reward, done, info = env.step(input.action)
    return {
        "state": state,
        "reward": reward,
        "done": done,
        "info": info
    }