import numpy as np


class KalmanFilter:
    def __init__(self, sensors, robot, sigma, acc_noise, dt, use_input=True):
        self.ts_prev = 0.0
        self._sensors = sensors
        self._time_vector = robot.time_vector
        self._system_input = robot.system_input
        self._can_predict = True
        self._last_time = 0
        self._use_input = use_input

        self._robot = robot
        self._x = np.array([[0.0],
                            [0.0]])

        self._P = np.array([[sigma[0]**2, 0],
                            [0, sigma[1]**2]])

        self._G = np.array([[0.5*dt**2],
                                   [dt]])

        self._Q = self._G @ self._G.T * acc_noise**2


    def estimate(self):
        time_vect_len = len(self._time_vector)
        estimated_state = np.zeros(time_vect_len)

        for i in range(time_vect_len):
            self._predict(i)
            for sensor in self._sensors:
                sensor.update()
                if sensor.data_available():
                    self._update(sensor)
                    sensor.reset_data_available()
            estimated_state[i] = self._robot.H @ self._x
        return estimated_state

    def P_in_time(self):
        return self._P_in_time

    def _predict(self, i):
        if self._use_input:
            self._x = self._robot.F @ self._x + self._robot.B * self._system_input[i]
        else:
            self._x = self._robot.F @ self._x
        self._P = self._robot.F @ self._P @ self._robot.F.T + self._Q


    def _update(self, sensor):
        K = self._P @ self._robot.H.T @ np.linalg.inv(self._robot.H @ self._P @ self._robot.H.T + sensor.R)
        self._x = self._x + K @ (sensor.z - self._robot.H @ self._x)
        self._P = (np.identity(len(K)) - K @ self._robot.H) @ self._P
