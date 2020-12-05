from collections import deque

import numpy as np

from sutton_barto_gym.envs.abstract.gridworld import Gridworld


class ClassicGridworld(Gridworld):
    """'Classic' Gridworld.

    Norvig & Russel (2020, 4th ed.).
    """

    def __init__(self):
        super().__init__(dims=(4, 3), start=(0, 0), blocks={(1, 1)})

    def step(self, action):
        assert self.action_space.contains(action)
        state = self._state
        reward = self._reward(state, action)
        done = self._done(state)
        info = {}

        if done:
            return self._encode(state), reward, done, info

        action = self._noisy_action(action)
        state = self._state = self._apply_move(state, action)
        return self._encode(state), reward, done, info

    def _noisy_action(self, action):
        x = np.random.rand()

        # 80% chance the action is unaffected
        if x < 0.8:
            return action

        # We use a deque for easy rotation
        all_actions = deque(self.actions())
        all_actions.rotate(-action)

        # 10% chance: rotate the action counter-clockwise
        if 0.8 <= x < 0.9:
            all_actions.rotate(1)
        # 10% chance: rotate the action clockwise
        else:
            all_actions.rotate(-1)

        return all_actions[action]

    def _reward(self, state, action):
        return {(3, 1): -1.0, (3, 2): 1.0}.get(state, 0.0)

    def _done(self, state):
        return state in {(3, 1), (3, 2)}

    def _generate_transitions(self, state, action):
        s = self._decode(state)

        all_actions = deque(self.actions())
        all_actions.rotate(-action)

        for i in [-1, 0, 1]:
            a = all_actions[i]
            ns = self._apply_move(s, a)
            prob = (0.8 if i == 0 else 0.1)
            yield self._encode(ns), self._reward(s, a), prob, self._done(s)
