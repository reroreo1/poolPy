class calculator:
    def __init__(self, arr: list[int]) -> None:
        self.vector = arr
#your code here
    def __add__(self, obj) -> None:
        for i in range(0,len(self.vector)):
            self.vector[i] += obj
        print(*self.vector)
    def __sub__(self, obj) -> None:
        for i in range(0,len(self.vector)):
            self.vector[i] -= obj
        print(*self.vector)
    def __mul__(self, obj) -> None:
        for i in range(0,len(self.vector)):
            self.vector[i] *= obj
        print(*self.vector)
    def __truediv__(self, obj) -> None:
        if obj == 0:
            raise ZeroDivisionError
        for i in range(0,len(self.vector)):
            self.vector[i] /= obj
        print(*self.vector)
