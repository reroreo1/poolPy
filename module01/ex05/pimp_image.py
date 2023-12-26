import numpy as np


def ft_invert(array) -> np.array:
    """invert the color of the image"""
    return 255 - array

def ft_red(array) -> np.array:
    """ set the green and blue channel to 0"""
    array[:, :, 0] = 0
    array[:, :, 1] = 0
    return array

def ft_green(array) -> np.array:
    """ set the red and blue channel to 0"""
    array[:, :, 0] = 0
    array[:, :, 2] = 0
    return array

def ft_blue(array) -> np.array:
    """ set the red and green channel to 0"""
    array[:, :, 1] = 0
    array[:, :, 2] = 0
    return array

def ft_grey(array) -> np.array:
    """makes the image grey"""
    grey_channel = array[:, :, 0]
    # Create a new array with the same shape as the original but with the red channel replicated
    grey_image = np.empty_like(array)
    grey_image[:, :, 1] = grey_channel
    grey_image[:, :, 0] = grey_channel
    grey_image[:, :, 2] = grey_channel  

    return grey_image