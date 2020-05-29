from kalman.sensor.sensor_interface import SensorInterface

import numpy as np

class Encoder(SensorInterface):
    def __init__(self, velocity):
        super().__init__()
