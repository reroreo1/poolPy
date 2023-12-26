import numpy as np
import cv2

def zoom(image_array: np.array, zoom_factor: float) -> np.array:
    # Get the dimensions of the image
    print("image shape before zoom: ", image_array.shape)
    print(image_array)
    height, width = image_array.shape[:2]
    # Calculate the size of the central region
    new_width, new_height = int(width / zoom_factor), int(height / zoom_factor)
    # Calculate the coordinates of the top-left corner of the central region
    x1, y1 = (width - new_width) // 2, (height - new_height) // 2
    # Extract the central region (ROI)
    roi = image_array[y1:y1+new_height, x1:x1+new_width]
    print("image shape after slicing",roi.shape)
    print(roi)
    # Resize the ROI back to the original image size
    zoomed_image = cv2.resize(roi, (width, height))
    cv2.imshow('image', zoomed_image) 
    cv2.waitKey(0) 
    cv2.destroyAllWindows() 
    return zoomed_image


