import cv2 as cv
import numpy as np
import sys

cap = cv.VideoCapture(0,cv.CAP_DSHOW)
cap_count = 0

if not cap.isOpened():
    sys.exit('카메라 연결 실패')

frames = []
while True:
    ret, frame = cap.read()

    if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break
    
    cv.imshow("Video display", frame)

    key = cv.waitKey(1)
    if key == ord('c'):
        cap_count += 1
        frame_small = cv.resize(frame, dsize=(0,0), fx=0.3, fy=0.3)
        frames.append(frame_small)
        print('저장성공! :',cap_count)

    elif key==ord('q'):
        break

cap.release()
cv.destroyAllWindows()

if len(frames)>0:
    imgs = frames[0]
    for i in range(1, min(3, len(frames))):
        imgs = np.hstack((imgs, frames[i]))
    print(f'해당 사진은 {i+1}번까지의 사진입니다')

    cv.imshow('collected images', imgs)

    cv.waitKey()
    cv.destroyAllWindows()