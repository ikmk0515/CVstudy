from PyQt5.QtWidgets import *
import sys
import cv2 as cv

class Video(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('비디오에서 프레임 수집') #윈도우 이름과 위치 지정
        self.setGeometry(200,200,600,150)  

        videoBtn = QPushButton('비디오 켜기',self)
        captureBtn = QPushButton('프레임 잡기',self)
        saveBtn = QPushButton('프레임 저장',self)
        quitBtn = QPushButton('나가기',self)

        videoBtn.setGeometry(10,10,100,30)
        captureBtn.setGeometry(110,10,100,30)
        saveBtn.setGeometry(210,10,100,30)
        quitBtn.setGeometry(310,10,100,30)

        videoBtn.clicked.connect(self.videoFunction)
        captureBtn.clicked.connect(self.captureFunction)
        saveBtn.clicked.connect(self.saveFunction)
        quitBtn.clicked.connect(self.quitFunction)

    def videoFunction(self):
        self.cap=cv.VideoCapture(0,cv.CAP_DSHOW)
        if not self.cap.isOpened(): self.close()

        while True:
            ret,self.frame=self.cap.read()
            if not ret: break
            cv.imshow('video display',self.frame)
            cv.waitKey(1)

    def captureFunction(self):
        self.capturedFrame=self.frame
        cv.imshow('Captured Frame',self.capturedFrame)

    def saveFunction(self):
        frame=QFileDialog.getSaveFileName(self,'파일 저장','./')
        cv.imwrite(frame[0],self.capturedFrame)

    def quitFunction(self):
        self.cap.release()
        cv.destroyAllWindows()
        self.close()

app=QApplication(sys.argv)
win=Video()
win.show()
app.exec_()