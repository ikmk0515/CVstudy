import matplotlib.pyplot as plt
import numpy as np
import cv2

if __name__ == '__main__':
    img_file = "img1.jpg"

    img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

    if img is not None:
        kernel = np.ones((3, 3), dtype=np.float64) / 9.
        kernel[0, :] = 1
        kernel[1, :] = 0
        kernel[2, :] = -1
        print(kernel)

        filtered_img = cv2.filter2D(img, -1, kernel)

        plt.imshow(filtered_img)
        plt.show()
