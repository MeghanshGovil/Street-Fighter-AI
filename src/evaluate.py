from src.environment import StreetFighterEnv
from src.agent import RLAgent

# Load trained model
env = StreetFighterEnv()
agent = RLAgent(env)
agent.model.load("models/best_model.pth")

# Run evaluation
observation = env.reset()
for _ in range(1000):
    action, _ = agent.predict(observation)
    observation, reward, done, _ = env.step(action)
    if done:
        break
