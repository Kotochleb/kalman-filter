import numpy as np


class KalmanFilter:
    def __init__(self, sensors, time_vector, process_noise, dt):
        self.ts_prev = 0.0
        self._sensors = sensors
        self._time_vector = time_vector
        self._can_predict = True

        self._x = np.array([0.0])
        self._P = np.array([0.5])
        self._Q = np.array([dt]) * process_noise
        self._F = np.array([1])

        self._P_in_time = np.zeros(len(self._time_vector))

    def estimate(self):
        time_vect_len = len(self._time_vector)
        estimated_state = np.zeros(time_vect_len)

        for i in range(time_vect_len):
            self._predict()
            for sensor in self._sensors:
                sensor.update()
                if sensor.data_available():
                    self._update(sensor)
                    sensor.reset_data_available()
            estimated_state[i] = self._x
            self._P_in_time[i] = self._P
        return estimated_state

    def P_in_time(self):
        return self._P_in_time

    def _predict(self):
        self._x = self._F * self._x
        self._P = self._F * self._P * self._F.T + self._Q


    def _update(self, sensor):
        S = sensor.H * self._P * sensor.H.T + sensor.R
        K = self._P * sensor.H.T * S**(-1)
        self._x = self._x + (K * (sensor.z - sensor.H * self._x))
        self._P = (1 - K * sensor.H) * self._P
        print(self._P, K)
