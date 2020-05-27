from kalman.sensor.abstract_sensor import AbstractSensor
import numpy as np


class GPS(AbstractSensor):

    def __init__(self, velocity):
        super().__init__(velocity)
        self.raw_velocity = velocity
        self._add_noise()
        self.x_location = np.trapz(self.raw_velocity)  # całkujemy velocity i mamy lokalizacje? o to nam chodzi?

    def data_available(self) -> bool:
        return self.x_location is not None

    @property
    def z(self):
        pass

    @property
    def h(self):
        pass

    @property
    def H(self):
        pass

    def update(self, Ts) -> None:
        pass

    def _add_noise(self):  # TODO jakie parametry szumu?
        noise = np.random.normal(0, 1, size=self.raw_velocity.size())
        self.raw_velocity += noise

