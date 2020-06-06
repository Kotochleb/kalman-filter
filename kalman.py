from kalman.sensor.encoder import Encoder
from kalman.sensor.gps import GPS
from kalman.sensor.imu import IMU
from kalman.sensor.dummySensor import DummySensor
from kalman.kalman_filter.kalman_filter import KalmanFilter
from kalman.state import state

import matplotlib.pyplot as plt
import numpy as np

v = lambda x: np.sin(0.5*x)

if __name__ == "__main__":

    fig = plt.figure()
    ax = fig.add_subplot()

    tv = np.arange(0, 30, 0.1)
    RS = state.RobotState(function=v, time_vector=tv)

    # sensors = [Encoder(RS), GPS(RS), IMU(RS)]
    sensors = [DummySensor(RS.vel_vect)]
    kf = KalmanFilter(sensors, tv)
    estimation = kf.estimate()

    ax.plot(RS.time_vector, RS.vel_vect, "--", linewidth=0.8, color="grey")
    ax.plot(RS.time_vector, estimation, linewidth=0.6)
    ax.plot(RS.time_vector, sensors[0].observation_in_time(), "--", linewidth=0.6)
    ax.legend(["True state", "Estimated state", "Observation"])
    ax.axes.set_xlabel("time [s]")
    ax.axes.set_ylabel("velocity [m/s]")
    plt.show()
