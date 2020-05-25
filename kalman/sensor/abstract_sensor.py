from abc import ABC

class AbstracSensor(ABC):
    def __init__(self, robot_path):
        raise NotImplementedError

    @abstractmethod
    def data_available(self):
        """
        Checks if there is available data on input buffer
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def z(self):
        """
        Returns observatoin vector
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def h(self):
        """
        Returns h vector. Don't ask me da hell is this. We gotta figure out
        return h: vector
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def H(self):
        """
        Returns H vector. Don't ask me da hell is this. We gotta figure out
        return H: matrix
        """
        raise NotImplementedError

    @abstractmethod
    def update(self, Ts):
        """
        Updates sensor in certain time
        param Ts: time sample
        returns none
        """
        raise NotImplementedError

    @abstractmethod
    def _add_noise(self):
        """
        Adds noise to input signal
        """
        raise NotImplementedError
