import torch
import numpy as np
from stable_baselines3 import PPO

class RLAgent:
    def __init__(self, env):
        self.env = env
        self.model = PPO("CnnPolicy", env, verbose=1)

    def train(self, num_episodes=5000):
        self.model.learn(total_timesteps=num_episodes)
        self.model.save("models/best_model.pth")

    def predict(self, observation):
        return self.model.predict(observation)
