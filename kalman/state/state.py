import numpy as np


class RobotState:
    def __init__(self, function, time_vector):
        self._time_vector = time_vector
        self._vel_vect = function(self._time_vector)

    @property
    def vel_vect(self):
        return self._vel_vect

    @property
    def time_vector(self):
        return self._time_vector
