from env import CloudEnv
from agent import Agent

env=CloudEnv()
agent=Agent()

state=env.reset()
for episode in range(20):
    action=agent.choose_option(state)
    next_state,reward,done,_=env.step(action)
    print(f"state:{state},action:{action},reward:{reward}")
    state=next_state