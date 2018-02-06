import math
import copy
import gym
from gym import spaces, logger
from gym.utils import seeding
import numpy as np

class GridWorldEnv(gym.Env) :
    metadata = {
        'render.modes' : ['human','rgb_array'],
        'video.frames_per_second' : 50
    }

    def __init__(self, **kwargs) :
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0.0, high=float(kwargs.get('dim',4)), shape=(2,))
        self.seed()
        self.viewer = None
        self._s = None
        self.steps_beyond_done = None
        self.action_effects = [ (1.0,0.0), (0.0,1.0), (-1.0,0.0), (0.0,-1.0) ]
        self.terminals = [ np.array([ self.observation_space[0].low, self.observation_space[1].high, \
            self.observation_space[0].high, self.observation_space[1].low ]) ]

    def seed( self, seed=None ) :
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    @property
    def state(self) :
        return self._s

    @state.setter
    def state(self, v) :
        self._s = copy.deepcopy(v)


    def step(self, action) :
        x,y = self._s
        dx, dy = self.action_effects[action]

        next_x = x + dx
        next_y = y + dy

        # Wraparound
        if self.observation_space.low[0] > next_x or
            self.observation_space.high[0] < next_x or
            self.observation_space.low[1] > next_y or
            self.observation_space.high[1] < next_y :
            next_x = x
            next_y = y

        self.state = np.array([next_x, next_y])

        reward = -1.0
        done = False
        if self.state in self.terminals :
            reward = 0.0
            done = True

        return self.state, reward, done, {}

    def reset(self, s = None) :
        if s is None :
            self._s = np.array([0.0, 0.0])
        else :
            self._s = copy.deepcopy(s)
        self.steps_beyond_done = None
        return self._s

    def render(self, mode='human'):
        pass

    def close(self):
        if self.viewer: self.viewer.close()
