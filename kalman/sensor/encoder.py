from kalman.sensor.abstract_sensor import AbstractSensor

import numpy as np

class Encoder(AbstractSensor):
    def __init__(self, velocity):
        super().__init__()
