from load_image import ft_load
from rotate import rotate
import cv2
def main():
    path = "./cat1.jpeg"
    image = ft_load(path)
    rotated_image = rotate(image)
    print(rotated_image)
    cv2.imshow('image', rotated_image) 
    cv2.waitKey(0) 
    cv2.destroyAllWindows() 


if __name__ == "__main__":
    main()