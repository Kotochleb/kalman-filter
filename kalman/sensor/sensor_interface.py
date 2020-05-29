from abc import ABC, abstractmethod


class SensorInterface(ABC):

    def __init__(self, velocity):
        pass

    @abstractmethod
    def data_available(self):
        """
        Checks if there is available data on input buffer
        """
        pass

    @property
    @abstractmethod
    def z(self):
        """
        Returns observation vector
        """
        pass

    @property
    @abstractmethod
    def h(self):
        """
        Returns h vector. Don't ask me da hell is this. We gotta figure out
        return h: vector
        """
        pass

    @property
    @abstractmethod
    def H(self):
        """
        Returns H vector. Don't ask me da hell is this. We gotta figure out
        return H: matrix
        """
        pass

    @abstractmethod
    def update(self):
        """
        Updates sensor in certain time
        param Ts: time sample
        returns none
        """
        pass

    @abstractmethod
    def _add_noise(self):
        """
        Adds noise to input signal
        """
        pass

    @abstractmethod
    def reset_data_available(self):
        """
        Resets sensor's data availability
        """
<<<<<<< HEAD:kalman/sensor/abstract_sensor.py
        pass
=======
        raise NotImplementedError
>>>>>>> 6291ffc0c66b6ded10c589a79c7cd59ee8b283ee:kalman/sensor/sensor_interface.py
