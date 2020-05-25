from kalman.sensor.encoder import Encoder
from kalman.sensor.gps import GPS
from kalman.sensor.imu import IMU

import numpy as np
import copy

# TODO change code to look not so suspicoius

class KalmanFilter:
    def __init__(self):
        self.ts_prev = 0.0

        # Placeholders
        self._x: Optional[np.ndarray] = np.array([0.])
        self._P: Optional[np.ndarray] = None
        self._F: Optional[np.ndarray] = None
        self._Q: Optional[np.ndarray] = None

        ############### to trzeba ogarnac #################3
        self.noise_vel = 3



    def predict(self):
        ######### TODO ############
        self._F = np.array([])
        nx = self.noise_vel

        ######### TODO ############
        self._Q = np.array([])

        self._x = self._F @ self._x
        self._P = self._F @ self._P @ self._F.T + self._Q




    def update(self, sensor):
        K = self._P @ H.T @ np.linalg.inv(sensor.H @ self._P @ sensor.H.T + sensor.R)
        self._x = self._x + (K @ (sensor.z - H @ sensor.h))
        I = (np.identity(len(self._x)))
        self._P = (I - K @ sensor.H) @ self._P
