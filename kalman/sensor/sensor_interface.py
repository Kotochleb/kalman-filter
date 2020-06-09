import abc


class SensorInterface(abc.ABC):

    def __init__(self, velocity):
        pass

    @abc.abstractmethod
    def data_available(self):
        """
        Checks if there is available data on input buffer
        """
        pass

    @property
    @abc.abstractmethod
    def z(self):
        """
        Returns observation vector
        """
        pass

    @property
    @abc.abstractmethod
    def R(self):
        """
        Returns R matrix of measurement noise.
        """
        pass

    @abc.abstractmethod
    def update(self):
        """
        Updates sensor in certain time
        param Ts: time sample
        returns none
        """
        pass

    @abc.abstractmethod
    def _add_noise(self):
        """
        Adds noise to input signal
        """
        pass

    @abc.abstractmethod
    def reset_data_available(self):
        """
        Resets sensor's data availability
        """
        pass

    @property
    @abc.abstractmethod
    def freq(self):
        """
        Returns sensor frequency
        """

    @abc.abstractmethod
    def observation_in_time(self):
        """
        Returns sensors observaction vector in time
        """
