from env import CloudEnv

env=CloudEnv()
state=env.reset()

for step in range(10):
    action=2
    state,reward,done, _=env.step(action)
    print(f"step {step}:state:{state},reward={reward}")