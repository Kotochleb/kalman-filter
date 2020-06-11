from kalman.sensor.sensor_interface import SensorInterface
from kalman.robot.robot import Robot
import numpy as np
from scipy import integrate
import copy


class IMU(SensorInterface):

    def __init__(self, rb: Robot):
        super().__init__(rb)
        self.raw_velocity = copy.copy(rb.vel_vect)
        self.index = 0  # indeks obecnie przetwarzanej probki danych
        self.noise_std = 0.05 # TODO jakie odchylenie standardowe szumu czujnika?
        self.frequency = 7  # czestotliwosc pracy czujnika
        self.acceleration = np.diff(self.raw_velocity)
        self.is_data_available = False
        self._add_noise()  # dodaj szum do acceleration
        self.vel = integrate.cumtrapz(self.acceleration, initial=0)


    def data_available(self) -> bool:
        return self.is_data_available

    @property
    def z(self):
        return self.vel[self.index-2]

    @property
    def R(self):
        return np.array([self.noise_std**2])

    @property
    def freq(self):
        return self.frequency

    def observation_in_time(self):
        return self.vel

    def update(self) -> None:
        self.index += 1
        if self.index % self.frequency == 0:
            self.is_data_available = True

    def _add_noise(self):
        self.noise = np.random.normal(0, self.noise_std, size=len(self.acceleration))
        self.acceleration += self.noise

    def reset_data_available(self):
        self.is_data_available = False

    def clear_counter(self):
        self._index = 0
