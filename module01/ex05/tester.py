from load_image import ft_load
from pimp_image import ft_blue
from pimp_image import ft_green
from pimp_image import ft_red
from pimp_image import ft_grey
from pimp_image import ft_invert
import cv2
def main():
    path = "./cat1.jpeg"
    image = ft_load(path)
    # blue_image = ft_blue(image)
    # green_image = ft_green(image)
    # red_image = ft_red(image)
    grey_image = ft_grey(image)
    # inverted_image = ft_invert(image)
    cv2.imshow('image', grey_image) 
    cv2.waitKey(0) 
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()