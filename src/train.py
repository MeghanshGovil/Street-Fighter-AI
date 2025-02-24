from src.environment import StreetFighterEnv
from src.agent import RLAgent

# Initialize environment
env = StreetFighterEnv()

# Initialize agent
agent = RLAgent(env)

# Train the agent
agent.train(num_episodes=5000)
