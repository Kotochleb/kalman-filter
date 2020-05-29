from kalman.sensor.sensor_interface import SensorInterface


class IMU(SensorInterface):

    def __init__(self, velocity):
        super().__init__()
