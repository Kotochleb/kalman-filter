from kalman.sensor.abstract_sensor import AbstractSensor

import numpy as np

class Encoder(AbstractSensor):
    def __init__(self, velocity, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frequency = 100  # to change
        self.noise_std = 3
        self.index = 0
        self.radius = 0.05 #circle's radius - 5cm
        self.velocity = velocity
        self.rotation_velocity = self.velocity / self.radius #array of rotation velocities
        self._add_noise()
        self._noised_velocity()
        self.is_data_available = True
        self.H = np.array([0, 0]) # TODO do implementacji - czekamy na szefa


    def _add_noise(self) -> None:
        self.noise = np.random.normal(0,self.noise_std, size = self.rotation_velocity.size())
        self.rotation_velocity += self.noise

    def _noised_velocity(self) -> None:
        self.rotation_velocity * self.radius

    @property
    def z(self):
        pass # TODO nie wiem co z macierza H nie implementowałem

    def reset_data_available(self) -> None:
        self.is_data_available = False

    def data_available(self) -> bool:
        return self.is_data_available

    def update(self) -> None:
        self.index += 1
        if self.index % self.frequency == 0:
            self.is_data_available = True