import numpy as np


class Robot:
    def __init__(self, function, time_vector, dt, d):
        self._time_vector = time_vector
        self._system_input = function(time_vector)

        self._F = np.array([[d, dt],
                            [0, 0]])

        self._B = np.array([[0],
                            [1]])

        self._H = np.array([[1, 0]])

        self._vel_vect = self._compute_state()

    @property
    def vel_vect(self):
        return self._vel_vect

    @property
    def time_vector(self):
        return self._time_vector

    @property
    def system_input(self):
        return self._system_input

    @property
    def F(self):
        return self._F

    @property
    def B(self):
        return self._B

    @property
    def H(self):
        return self._H


    def _compute_state(self):
        vel_vect = np.zeros(len(self._time_vector),dtype=np.float32)
        state = self._B * self._system_input[0]
        for i in range(1,(len(self._time_vector)-1)):
            state = self._F @ state + self._B * self._system_input[i]
            vel_vect[i] = self._H @ state

        return vel_vect
