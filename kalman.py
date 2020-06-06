from kalman.sensor.encoder import Encoder
from kalman.sensor.gps import GPS
from kalman.sensor.imu import IMU
from kalman.sensor.dummySensor import DummySensor
from kalman.kalman_filter.kalman_filter import KalmanFilter
from kalman.state import state

import matplotlib.pyplot as plt
import numpy as np

v = lambda x: 20*np.heaviside(x-30, 0) - 10*np.heaviside(x-70, 0) + 10*np.sin(0.1*(x-100))*np.heaviside(x-100, 0)


if __name__ == "__main__":

    fig, axs = plt.subplots(3)

    tv = np.arange(0, 150, 0.25)
    RS = state.RobotState(function=v, time_vector=tv)

    # sensors = [Encoder(RS), GPS(RS), IMU(RS)]
    sensors = [DummySensor(RS.vel_vect, 2, 7), DummySensor(RS.vel_vect, 10, 4), DummySensor(RS.vel_vect, 50, 0.04)]
    kf = KalmanFilter(sensors, tv, 0.01)
    estimation = kf.estimate()

    axs[0].plot(RS.time_vector, RS.vel_vect, "--", linewidth=1, color="grey")
    axs[0].plot(RS.time_vector, estimation, linewidth=0.7)
    for sensor in sensors:
        axs[0].plot(RS.time_vector[0::sensor.freq], sensor.observation_in_time()[0::sensor.freq], "--", linewidth=0.2)
    axs[0].legend(["True state", "Estimated state", "Encoder", "IMU", "GPS"])
    axs[0].axes.set_xlabel("time [s]")
    axs[0].axes.set_ylabel("velocity [m/s]")
    
    axs[1].plot(RS.time_vector, kf.P_in_time(), linewidth=0.5)
    axs[1].axes.set_xlabel("time [s]")
    axs[1].axes.set_ylabel("covariance")

    axs[2].plot(RS.time_vector, RS.vel_vect - estimation, linewidth=0.5)
    axs[2].plot(RS.time_vector, np.zeros(len(RS.time_vector)), "--", linewidth=0.5, color="grey")
    axs[2].axes.set_xlabel("time [s]")
    axs[2].axes.set_ylabel("error")
    plt.show()
