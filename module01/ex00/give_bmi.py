import numpy as np


def give_bmi(height: list[int | float],
weight: list[int | float])-> list[int | float]:
#your code here
    return list(np.array(weight) /
    np.power(np.array(height), 2))
def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return np.array(bmi) > limit
#your code here





