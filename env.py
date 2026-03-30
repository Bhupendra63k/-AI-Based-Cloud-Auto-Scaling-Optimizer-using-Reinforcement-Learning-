import random

class CloudEnv:
    def __init__(self):
        self.max_server=10
        self.min_server=1
        self.reset()
    
    def reset(self):
        self.cpu=random.randint(30,70)
        self.servers=3
        self.traffic=random.randint(200,1000)
        return self.get_state()
    
    def step(self,action):
        penalty=0
        if action==0:
            if self.servers==self.min_server:
                penalty=-5
            self.servers=max(self.min_server,self.servers-1)
        elif action==2:
            if self.servers==self.max_server:
                penalty=-5
            self.servers=min(self.max_server,self.servers+1)
        
        self.traffic+=random.randint(-100,150)
        self.traffic=max(50,self.traffic)

        self.cpu=min(100,self.traffic/(self.servers*15))
        cost=self.servers*2
        latency=self.cpu*1.5

        if self.cpu >85:
            reward=-15
            if action==2:
                reward=+15
        elif self.cpu<30:
            reward=-5
            if action==0:
                reward=+10
        elif 40<=self.cpu<=70:
            reward=+15
        else:
            reward=+5
        
        if self.cpu<30 and action==0:
            reward=+20
        
        if self.cpu>70 and action==2:
            reward=+20
        if self.cpu>70 and action!=2:
            reward=-20
        
        reward-=cost*0.3
        reward-=latency*0.02
        
        done=False
        reward += penalty
        return self.get_state(),reward,done,{}
    
    def get_state(self):
        if self.cpu<30:
            cpu_state=0
        elif self.cpu<70:
            cpu_state=1
        else:
            cpu_state=2
        return (cpu_state,self.servers)

