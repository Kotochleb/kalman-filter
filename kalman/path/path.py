import numpy as np


class RobotPath:
    def __init__(self, function, time, Ts, offset=0):
        self._vel = function(np.arange(offset, time, Ts))

    @property
    def vel(self):
        return self._vel
