import cv2 as cv
import sys

img = cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

cv.imshow('original_RGB', img)
cv.imshow('Upper left half', img[0:img.shape[0]//2,0:img.shape[1]//2])