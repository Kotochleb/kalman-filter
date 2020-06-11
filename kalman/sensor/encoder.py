from kalman.sensor.sensor_interface import SensorInterface
from kalman.robot.robot import Robot
from scipy import integrate
import numpy as np


class Encoder(SensorInterface):
    def __init__(self, rb: Robot):
        super().__init__(rb.vel_vect)
        self._frequency = 3
        self._noise_std = 0.3
        self._index = 0
        self._radius = 0.05 #circle's radius - 5cm
        self._velocity = rb.vel_vect
        self._rotation_velocity = self._velocity / self._radius #array of rotation velocities
        self._add_noise()
        self._noised_velocity()
        self._is_data_available = False

    def data_available(self) -> bool:
        return self._is_data_available

    @property
    def z(self):
        return self._velocity[self._index - 2]

    @property
    def R(self):
        return np.array([self._noise_std ** 2])

    @property
    def H(self):
        return np.array([1])

    @property
    def freq(self):
        return self._frequency

    def observation_in_time(self):
        return self._velocity

    def update(self) -> None:
        self._index += 1
        if self._index % self._frequency == 0:
            self._is_data_available = True

    def _add_noise(self) -> None:
        self.noise = np.random.normal(0,self._noise_std, size = len(self._rotation_velocity))
        self._rotation_velocity += self.noise

    def _noised_velocity(self) -> None:
        self._rotation_velocity * self._radius

    def reset_data_available(self) -> None:
        self._is_data_available = False

    def clear_counter(self):
        self._index = 0
