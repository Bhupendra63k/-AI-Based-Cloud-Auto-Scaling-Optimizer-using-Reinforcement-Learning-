import gradio as gr
from env import CloudEnv
import random

env = CloudEnv()

def simulate(steps):
    state = env.reset()
    output = []

    for _ in range(steps):
        action = random.choice([0,1,2])  # demo agent
        state, reward, _, _ = env.step(action)
        output.append(f"State: {state}, Reward: {round(reward,2)}")

    return "\n".join(output)

interface = gr.Interface(
    fn=simulate,
    inputs=gr.Slider(10, 100, value=50, label="Steps"),
    outputs="text",
    title="AI Cloud Auto-Scaling Environment",
    description="Simulates scaling decisions with cost, latency, and CPU optimization."
)

interface.launch()