import abc
from abc import ABC
from MyMixin import MyMixin


class GeometricFigure(ABC, MyMixin):
    @abc.abstractmethod
    def get_area(self):
        pass
