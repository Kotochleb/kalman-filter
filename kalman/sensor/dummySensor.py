from kalman.sensor.sensor_interface import SensorInterface
import numpy as np
import copy


class DummySensor(SensorInterface):

    def __init__(self, velocity, freq, std):
        self._idx = 0
        self._freq = freq
        self.is_data_available = False
        self.noise_std = std
        self._x = copy.copy(velocity)
        self._add_noise()

    def data_available(self):
        return self.is_data_available

    @property
    def z(self):
        return self._x[self._idx-1]

    @property
    def R(self):
        return np.array([self.noise_std**2])

    @property
    def H(self):
        return np.array([1])

    @property
    def freq(self):
        return self._freq

    def observation_in_time(self):
        return self._x

    def update(self):
        self._idx += 1
        if self._idx % self._freq == 0:
            self.is_data_available = True

    def _add_noise(self):
        self._x += np.random.normal(0, self.noise_std, size=len(self._x))

    def reset_data_available(self):
        self.is_data_available = False
