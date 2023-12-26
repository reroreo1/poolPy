import numpy as np



def slice_me(family: list, start: int, end: int) -> list:
    arr = np.array(family)
    print("my shape is ", arr.shape)
    arr = arr[start:end]
    print("my new shape is ", arr.shape)
    return arr.tolist()