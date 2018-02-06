import math
import gym
from gym import spaces, logger
from gym.utils import seeding
import numpy as np

class GridWorld(gym.Env) :
    metadata = {
        'render.modes' : ['human','rgb_array'],
        'video.frames_per_second' : 50
    }

    def __init__(self, **kwargs) :
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0.0, high=float(kwargs.get('dim',4)), shape=(2,))
        self.seed()
        self.viewer = None
        self.state = None
        self.steps_beyond_done = None

    def seed( self, seed=None ) :
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action) :
        pass

    def reset(self) :
        self.state = np.array([0.0, 0.0])
        self.steps_beyond_done = None
        return self.state

    def render(self, mode='human'):
        pass

    def close(self):
        if self.viewer: self.viewer.close()
