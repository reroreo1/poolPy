def square(x: int | float) -> int | float:
#your code here
    return x**2

def pow(x: int | float) -> int | float:
#your code here
    return x**x


def outer(x: int | float, function) -> callable:

    def inner() -> float:
        nonlocal x
        count = function(x)
        x = count
        return x

    return inner
