from S1E7 import Lannister, Baratheon


class King(Lannister, Baratheon):
    """class that represents the king it inherits from lannister and baratheon"""
    def __init__(self, name: str, is_alive: bool = True):
        # Call to parent class initializers should pass 'self' as the first argument
        Lannister.__init__(self, name, is_alive)
        Baratheon.__init__(self, name, is_alive)

    def set_eyes(self, color: str):
        """eyes setter"""
        self.eyes = color

    def set_hairs(self, hairs: str):
        """hairs setters"""
        self.hairs = hairs

    def get_eyes(self):
        """eyes getter"""
        return self.eyes

    def get_hairs(self):
        """hairs getter"""
        return self.hairs
