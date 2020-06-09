from kalman.sensor.sensor_interface import SensorInterface
from kalman.robot.robot import Robot
from scipy import integrate
import numpy as np
import copy


class GPS(SensorInterface):

    def __init__(self, rb: Robot):
        super().__init__(rb.vel_vect)
        self._raw_velocity = copy.copy(rb.vel_vect)
        self._position = integrate.cumtrapz(self._raw_velocity, initial=0)
        self._index = 0  # indeks obecnie przetwarzanej probki danych
        self._noise_std = 0.001
        self._frequency = 30  # czestotliwosc pracy czujnika
        self.is_data_available = False
        self._add_noise()  # dodaj szum do position
        self._velocity = np.diff(self._position)

    def data_available(self) -> bool:
        return self.is_data_available

    @property
    def z(self):
        return self._velocity[self._index-2]

    @property
    def R(self):
        return np.array([self._noise_std**2])

    @property
    def freq(self):
        return self._frequency

    def observation_in_time(self):
        return self._velocity

    def update(self) -> None:
        self._index += 1
        if self._index % self._frequency == 0:
            self.is_data_available = True

    def _add_noise(self) -> None:
        self.noise = np.random.normal(0, self._noise_std, size=len(self._position))
        self._position += self.noise

    def reset_data_available(self):
        self.is_data_available = False
