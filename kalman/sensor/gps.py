from kalman.sensor.abstract_sensor import AbstractSensor
import numpy as np


class GPS(AbstractSensor):

    def __init__(self, velocity):
        super().__init__(velocity)
        self.position = np.cumsum(velocity)
        self.index = 0  # indeks obecnie przetwarzanej probki danych
        self.noise_std = 1  # TODO jakie odchylenie standardowe szumu czujnika?
        self.frequency = 2  # czestotliwosc pracy czujnika
        self.is_data_available = True
        self._add_noise()  # dodaj szum do position

    def data_available(self) -> bool:
        return self.is_data_available

    @property
    def z(self):
        # TODO oblicz z i go zwroc
        pass

    @property
    def h(self):
        # TODO oblicz h i go zwroc
        pass

    @property
    def H(self):
        # TODO oblicz H i ja zwroc
        pass

    def update(self) -> None:
        self.index += 1
        if self.index % self.frequency == 0:
            self.is_data_available = True

    def _add_noise(self) -> None:
        noise = np.random.normal(0, self.noise_std, size=self.position.size())
        self.position += noise

    def reset_data_available(self):
        self.is_data_available = False
