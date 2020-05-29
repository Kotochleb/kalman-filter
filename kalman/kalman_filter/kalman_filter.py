from kalman.sensor.encoder import Encoder
from kalman.sensor.gps import GPS
from kalman.sensor.imu import IMU

import numpy as np
import copy


class KalmanFilter:
    def __init__(self, sensors, time_vector):
        self.ts_prev = 0.0
        self._sensors = sensors
        self._time_vector = time_vector

        # Placeholders
        self._x = np.array([0.0])
        self._P = None
        self._F = None
        self._Q = None

        ############### to trzeba ogarnac #################3
        self.vel_noise = 3

        self._is_initialized = False

    def estimate(self):

        if not self._is_initialized:
            self._initialize()

        time_vect_len = len(self._time_vector)
        estimated_state = np.zeros(time_vect_len)

        for i in range(time_vect_len):
            for sensor in self._sensors:
                sensor.update()
                if sensor.data_available():
                    self._update(sensor)
                else:
                    self._predict()
            estimated_state[i] = self._x

        return estimated_state


    def _initialize(self):
        raise NotImplementedError


    def _predict(self):
        ######### TODO ############
        self._F = np.array([])
        nx = self.vel_noise

        ######### TODO ############
        self._Q = np.array([])

        self._x = self._F @ self._x
        self._P = self._F @ self._P @ self._F.T + self._Q


    def _update(self, sensor):
        K = self._P @ H.T @ np.linalg.inv(sensor.H @ self._P @ sensor.H.T + sensor.R)
        self._x = self._x + (K @ (sensor.z - H @ sensor.h))
        I = (np.identity(len(self._x)))
        self._P = (I - K @ sensor.H) @ self._P
