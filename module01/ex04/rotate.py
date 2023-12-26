import numpy as np
def rotate(arr: np.array)->np.array:
    print("my shape is ", arr.shape)
    square_size = min(arr.shape[0], arr.shape[1])
    print("my square size is ", square_size)
    arr = arr[:square_size, :square_size]
    return arr.transpose(1,0,2)