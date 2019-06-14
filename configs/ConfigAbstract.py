# Python 3.4+
from abc import ABC, abstractmethod
class ConfigAbstract(ABC):

    @abstractmethod
    def getRangeSize(self):
        pass