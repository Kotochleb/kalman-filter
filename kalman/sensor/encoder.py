from kalman.sensor.sensor_interface import SensorInterface

import numpy as np

class Encoder(SensorInterface):
    def __init__(self, velocity, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._frequency = 100  # to change
        self._noise_std = 3
        self._index = 0
        self._radius = 0.05 #circle's radius - 5cm
        self._velocity = velocity
        self._rotation_velocity = self._velocity / self._radius #array of rotation velocities
        self._add_noise()
        self._noised_velocity()
        self._is_data_available = True
        self._H = np.array([0, 1]) # TODO do implementacji - czekamy na szefa


    def _add_noise(self) -> None:
        self.noise = np.random.normal(0,self._noise_std, size = self._rotation_velocity.size())
        self._rotation_velocity += self.noise

    def _noised_velocity(self) -> None:
        self._rotation_velocity * self._radius

    @property
    def z(self):
        pass # TODO nie wiem co z macierza H nie implementowałem

    def reset_data_available(self) -> None:
        self._is_data_available = False

    def data_available(self) -> bool:
        return self._is_data_available

    def update(self) -> None:
        self._index += 1
        if self._index % self._frequency == 0:
            self._is_data_available = True
