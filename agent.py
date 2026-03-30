import random

class Agent:
    def __init__(self):
        self.q_table={}
        self.alpha=0.5
        self.gamma=0.9
        self.epsilon=0.3
    
    def get_p(self,state,action):
        return self.q_table.get(tuple(state),[0,0,0])[action]
    
    def choose_option(self,state):
        state=tuple(state)
        if state not in self.q_table:
            self.q_table[state]=[0,0,0]
        
        if random.random()<self.epsilon:
            return random.choice([0,1,2])
        q_value=self.q_table[state]
        max_q=max(q_value)
        best_actions=[i for i,q in enumerate(q_value) if q==max_q]
        return random.choice(best_actions)
    
    def learn(self,state,action,reward,next_state):
        state=tuple(state)
        next_state=tuple(next_state)

        if state not in self.q_table:
            self.q_table[state]=[0,0,0]
        
        if next_state not in self.q_table:
            self.q_table[next_state]=[0,0,0]
        
        current_q=self.q_table[state][action]
        max_next_q=max(self.q_table[next_state])

        new_q=current_q+self.alpha*(reward+self.gamma*max_next_q-current_q)
        self.q_table[state][action]=new_q
