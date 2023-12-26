import cv2
import numpy as np


def ft_load(path: str)-> np.array:
    image = cv2.imread(path)
    image1 = np.array(image)
    print("the shape of the image is: ",image1.shape)
    return image1
