from kalman.sensor.encoder import Encoder
from kalman.sensor.gps import GPS
from kalman.sensor.imu import IMU
from kalman.sensor.dummySensor import DummySensor
from kalman.kalman_filter.kalman_filter import KalmanFilter
from kalman.robot.robot import Robot

import matplotlib.pyplot as plt
import numpy as np

v = lambda x: 0.3*(np.heaviside(x-20, 0) - np.heaviside(x-50,  0))
if __name__ == "__main__":

    fig, axs = plt.subplots(2)
    dt = 0.5

    tv = np.arange(0, 150, dt)
    rb = Robot(function=v, time_vector=tv, dt=dt, d=0.95)

    sensors = [Encoder(rb), IMU(rb), GPS(rb)]
    # sensors = [DummySensor(rb, 1, 0.6), DummySensor(rb, 8, 0.2), DummySensor(rb, 30, 0.01)]
    kf = KalmanFilter(sensors, rb, [0.2, 0.2], 0.3, dt, use_input=True)
    estimation = kf.estimate()

    axs[0].plot(rb.time_vector, rb.system_input, "--", linewidth=0.4, color="black")
    axs[0].axes.set_ylabel("acceleration")
    axs[1].plot(rb.time_vector, rb.vel_vect, "--", linewidth=1, color="grey")
    axs[1].plot(rb.time_vector, estimation, linewidth=0.7)
    for sensor in sensors:
        axs[1].plot(rb.time_vector[0::sensor.freq], sensor.observation_in_time()[0::sensor.freq], "--", linewidth=0.5)
    axs[1].legend(["True state", "Estimated steate", "Encoder", "Acceleratometer", "GPS"])
    axs[1].axes.set_xlabel("time")
    axs[1].axes.set_ylabel("velocity")
    # axs[2].plot(rb.time_vector, estimation-rb.vel_vect, linewidth=0.5)
    # axs[2].plot(rb.time_vector, np.zeros(len(rb.time_vector)), "--", linewidth=0.5, color="grey")
    # axs[2].axes.set_xlabel("time")
    # axs[2].axes.set_ylabel("error")
    plt.show()
