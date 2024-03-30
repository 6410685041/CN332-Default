from abc import ABC, abstractmethod
import turtle as t

class Color(ABC):
    @abstractmethod
    def fill(self):
        pass

class Red(Color):
    def __init__(self, color):
        self.color = color

    def fill(self):
        pass

class Blue(Color):
    def __init__(self, color):
        self.color = color

    def fill(self):
        pass

class Green(Color):
    def __init__(self, color):
        self.color = color

    def fill(self):
        pass