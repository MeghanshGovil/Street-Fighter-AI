import retro
import gym

class StreetFighterEnv:
    def __init__(self):
        self.env = retro.make(game="StreetFighterIISpecialChampionEdition-Genesis")

    def reset(self):
        return self.env.reset()

    def step(self, action):
        return self.env.step(action)

    def render(self):
        self.env.render()
