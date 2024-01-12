from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self,name: str, is_alive: bool = True):
        super().__init__(name)
        self.family_name = "Baratheon"
        self.eyes = 'brown'
        self.hairs = 'dark'
    def __str__(self) -> str:
        return f'Vector of : ({self.family_name}, {self.eyes}, {self.hairs})'
    def __repr__(self) -> str:
        return f'Vector of : {self.family_name}, {self.eyes}, {self.hairs}'
    def die(self):
        """changes the health status of the character"""
        self.is_alive = False
    @classmethod
    def create_baratheon(cls, name: str,is_alive: bool = True):
        """ a class method that creates characters in chain"""
        return Baratheon(name,is_alive)
    #your code here

# class Lannister(Character):
#     #your code here
#     # decorator
#     def create_lannister(your code here):
class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self,name: str, is_alive: bool = True):
        super().__init__(name)
        self.family_name = "Lannister"
        self.eyes = 'blue'
        self.hairs = 'light'
    def __str__(self) -> str:
        return f'Vector of : ({self.family_name}, {self.eyes}, {self.hairs})'
    def __repr__(self) -> str:
        return f'Vector of : ({self.family_name}, {self.eyes}, {self.hairs})'
    def die(self):
        """changes the health status of the character"""
        self.is_alive = False
    @classmethod
    def create_lannister(cls, name: str,is_alive: bool = True):
        """ a class method that creates characters in chain"""
        return Lannister(name, is_alive)