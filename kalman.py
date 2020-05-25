from kalman.sensor.encoder import Encoder
from kalman.sensor.gps import GPS
from kalman.sensor.imu import IMU
from kalman.kalman_filter.kalman_filter import KalmanFilter
from kalman.path import path

import matplotlib.pyplot as plt
import numpy as np

v = lambda x: np.sin(x)

if __name__ == "__main__":
    RP = path.RobotPath(v, 3, 0.1)

    kf = KalmanFilter()

    encoder = Encoder(RP.vel)

    # trzeba dac jaki sensowniejszy warynek wyjsia
    # zalezny od konca danych
    while True:
        encoder.update()
        if encoder.data_available():
            kf.update(encoder)
        else:
            kf.predict()
