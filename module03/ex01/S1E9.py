from abc import ABC, abstractmethod


class Character(ABC):
    """an abstract class to represent a character"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """initialize the character"""
        self.first_name = first_name
        self.is_alive = is_alive
    @abstractmethod
    def die(self):
        """changes the health status of the character"""
        self.is_alive = False

class Stark(Character):
    """a class to represent the Stark family that inherits from Character"""
    def die(self):
        """changes the health status of the Stark family"""
        self.is_alive = False
