from kalman.sensor import abstract_sensor

import numpy as np

class encoder(AbstractSensor):
    def __init__(self, velocity):
        Super().__init__()
