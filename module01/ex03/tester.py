from load_image import ft_load
from zoom import zoom

def main():
    path = "./cat1.jpeg"
    image = ft_load(path)
    zoomed_image = zoom(image, 1)
    print(image)


if __name__ == "__main__":
    main()