from env import CloudEnv
from agent import Agent
import matplotlib.pyplot as plt

env = CloudEnv()
agent = Agent()

episodes = 4000

# -------------------
# TRAINING
# -------------------
for episode in range(episodes):
    state = env.reset()

    for step in range(100):
        action = agent.choose_option(state)
        next_state, reward, done, _ = env.step(action)

        agent.learn(state, action, reward, next_state)

        state = next_state

    # optional epsilon decay
    agent.epsilon *= 0.995

print("Training Done")

# -------------------
# TEST PHASE (IMPORTANT 🔥)
# -------------------
agent.epsilon = 0  # no randomness

cpu_history = []
server_history = []
reward_history = []

state = env.reset()

for _ in range(200):   # small clean run
    action = agent.choose_option(state)
    next_state, reward, _, _ = env.step(action)

    cpu_history.append(env.cpu)
    server_history.append(env.servers)
    reward_history.append(reward)

    state = next_state

# -------------------
# GRAPHS
# -------------------

# CPU
plt.figure()
plt.plot(cpu_history)
plt.title("CPU Usage Over Time")
plt.xlabel("Steps")
plt.ylabel("CPU")
plt.show()

# Servers
plt.figure()
plt.plot(server_history)
plt.title("Server Count Over Time")
plt.xlabel("Steps")
plt.ylabel("Servers")
plt.show()

# Reward
plt.figure()
plt.plot(reward_history)
plt.title("Reward Over Time")
plt.xlabel("Steps")
plt.ylabel("Reward")
plt.show()