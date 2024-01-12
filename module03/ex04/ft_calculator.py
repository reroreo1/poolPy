class calculator:
    def __init__(self, arr: list[float]) -> None:
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
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        print("Dot product is :",sum(V1[i] * V2[i] for i in range(0,3)))
    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        print("Add Vector is :",[float(V1[i] + V2[i]) for i in range(0,3)])
    #your code here
    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        print("Sous Vector is :",[float(V1[i] - V2[i]) for i in range(0,3)])
