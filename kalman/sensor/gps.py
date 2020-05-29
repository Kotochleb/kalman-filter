from kalman.sensor.sensor_interface import SensorInterface
import numpy as np


class GPS(SensorInterface):

    def __init__(self, velocity):
        super().__init__(velocity)
        self.raw_velocity = velocity
        self.position = np.cumsum(self.raw_velocity)
        self.index = 0  # indeks obecnie przetwarzanej probki danych
        self.noise_std = 1  # TODO jakie odchylenie standardowe szumu czujnika?
        self.frequency = 2  # czestotliwosc pracy czujnika
        self.is_data_available = True
        self.H = np.array([1, 0])  # tak bylo na forbocie, nie wiem czy dobrze
        self._add_noise()  # dodaj szum do position

    def data_available(self) -> bool:
        return self.is_data_available

    @property
    def z(self):  # nie wiem czy w getterze powinno sie definiowac property, pewnie nie
        x_k = np.array([self.position], [self.raw_velocity])  # wektor stanu
        self.z = np.dot(self.H, x_k) + self.noise
        return self.z

    @property
    def h(self):  # nie mam pojecia czym jest h, nie widze go na forbocie nawet
        # TODO oblicz h i go zwroc
        pass

    @property
    def H(self):
        return self.H

    def update(self) -> None:
        self.index += 1
        if self.index % self.frequency == 0:
            self.is_data_available = True

    def _add_noise(self) -> None:
        self.noise = np.random.normal(0, self.noise_std, size=self.position.size())
        self.position += self.noise

    def reset_data_available(self):
        self.is_data_available = False
