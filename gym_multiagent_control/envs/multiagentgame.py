import gym
import random
import numpy as np


#env_name = "CartPole-v1"
#env_name = "MountainCar-v0"
#env_name = "MountainCarContinuous-v0"
#env_name = "Acrobot-v1"
#env_name = "Pendulum-v0"

env = gym.make("gym_multiagent_control:foo-v1")
print("Observation space:", env.observation_space)
print("Action space:", env.action_space)
type(env.action_space)


class Agent():
    def __init__(self, env):
        self.is_discrete = \
            type(env.action_space) == gym.spaces.discrete.Discrete
        
        if self.is_discrete:
            self.action_size = env.action_space.n
            print("Action size:", self.action_size)
        else:
            self.action_low = env.action_space.low
            self.action_high = env.action_space.high
            self.action_shape = env.action_space.shape
            print("Action range:", self.action_low, self.action_high)
        
    def get_action(self, state):
        if self.is_discrete:
            action = random.choice(range(self.action_size))
        else:
            action = np.random.uniform(self.action_low,
                                       self.action_high,
                                       self.action_shape)
        return action
    
agent = Agent(env)
state = env.reset()

for _ in range(100000):
#     action = env.action_space.sample()
    action = agent.get_action(state)
    state, reward, done, info = env.step(action)
    env.render()