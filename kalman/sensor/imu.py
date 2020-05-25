from kalman.sensor.abstract_sensor import AbstractSensor


class IMU(AbstractSensor):

    def __init__(self, velocity):
        super().__init__()