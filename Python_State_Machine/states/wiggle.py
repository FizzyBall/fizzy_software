"""
Oscillatory wiggle motion.
"""

import time
import numpy as np

from states.base import State


class Wiggle(State):

    def __init__(self, T1, T2, A1, A2, duration=5):

        super().__init__(duration)

        self.T1 = T1
        self.T2 = T2
        self.A1 = A1
        self.A2 = A2

        # Total oscillation cycle time
        self.cycle = T1 + T2 + T1

    def update(self, dt, sensors, joystick):

        # Time inside oscillation cycle
        t = (time.time() - self.start_time) % self.cycle
        # print("Wiggle")
        # Piecewise cosine trajectory
        if t < self.T1:
            return self.A1 * np.cos(np.pi * t / self.T1)

        elif t < self.T1 + self.T2:
            return self.A2 * np.cos(np.pi * (t-self.T1) / self.T2)

        else:
            return self.A1 * np.cos(np.pi * (t-self.T1-self.T2) / self.T1)
