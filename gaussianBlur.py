import matplotlib.pyplot as plt
import numpy as np
import cv2

if __name__ == "__main__":
    img_file = "img1.jpg"
    img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

    if img is not None:
        gaussian_img1 = cv2.GaussianBlur(img, (0, 0), 1)
        gaussian_img2 = cv2.GaussianBlur(img, (0, 0), 2)
        gaussian_img3 = cv2.GaussianBlur(img, (0, 0), 3)

        plt.subplot(2, 2, 1)
        plt.title("original")
        plt.imshow(img, cmap='gray')

        plt.subplot(2, 2, 2)
        plt.title("sigma = 1")
        plt.imshow(gaussian_img1, cmap='gray')
        plt.subplot(2, 2, 3)
        plt.title("sigma = 2")
        plt.imshow(gaussian_img2, cmap='gray')
        plt.subplot(2, 2, 4)
        plt.title("sigma = 3")
        plt.imshow(gaussian_img3, cmap='gray')

        plt.show()
