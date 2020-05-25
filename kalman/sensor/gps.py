from kalman.sensor.abstract_sensor import AbstractSensor


class GPS(AbstractSensor):

    def __init__(self, velocity):
        super().__init__()