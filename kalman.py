from kalman.sensor.encoder import Encoder
from kalman.sensor.gps import GPS
from kalman.sensor.imu import IMU
from kalman.kalman_filter.kalman_filter import KalmanFilter
from kalman.state import state

import matplotlib.pyplot as plt
import numpy as np

v = lambda x: np.sin(x)

if __name__ == "__main__":

    fig = plt.figure()
    ax = fig.add_subplot()

    tv = np.arange(0, 3, 0.1)
    RP = state.RobotState(function=v, time_vector=tv)

    # TODO docelowo to bedzie w ten sposob. Chwilowo trzeba
    # zaimplementowac czujniki wiec zostaje puste
    # sensors = [Encoder(RP), GPS(RP), IMU(RP)]
    sensors = []
    kf = KalmanFilter(sensors, tv)
    estimation = kf.estimate()

    ax.plot(RP.time_vector, RP.vel_vect, "--", linewidth=0.8, color="grey")
    ax.plot(RP.time_vector, estimation)
    ax.legend(["True state", "Esymated state"])
    ax.axes.set_xlabel("time [s]")
    ax.axes.set_ylabel("velocity [m/s]")
    plt.show()
