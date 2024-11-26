import cv2 as cv
import numpy as np
import sys
from PyQt5.QtWidgets import *

class Orim(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('오림')
        self.setGeometry(200,200,700,200)
    
        # 버튼 선언
        fileBtn=QPushButton('파일',self)
        paintBtn=QPushButton('페인팅',self)
        cutBtn=QPushButton('오림',self)
        incBtn=QPushButton('+',self)
        decBtn=QPushButton('-',self)
        saveBtn=QPushButton('저장',self)
        quitBtn=QPushButton('나가기',self)

        # 버튼 위치 및 크기 설정
        fileBtn.setGeometry(10,10,100,30)
        paintBtn.setGeometry(110,10,100,30)
        cutBtn.setGeometry(210,10,100,30)
        incBtn.setGeometry(310,10,100,30)
        decBtn.setGeometry(360,10,100,30)
        saveBtn.setGeometry(410,10,100,30)
        quitBtn.setGeometry(510,10,100,30) 

        # 콜백 함수 지정
        fileBtn.clicked.connect(self.fileOpenF)
        paintBtn.clicked.connect(self.paintF)
        cutBtn.clicked.connect(self.cutF)
        incBtn.clicked.connect(self.incF)
        decBtn.clicked.connect(self.decF)
        saveBtn.clicked.connect(self.saveF)
        quitBtn.clicked.connect(self.quitF)

        self.BrushSize=5
        self.LColor,self.RColor=(255,0,0),(0,0,255)   

    def fileOpenF(self):
        fname=QFileDialog.getOpenFileName(self,'Open file','./')
        self.img=cv.imread(fname[0])
        

    def paintF(self):
        pass

    def painting(self):
        pass

    def cutF(self):
        pass
    
    def incF(self):
        pass

    def decF(self):
        pass

    def saveF(self):
        pass
    
    def quitF(self):
        pass

app=QApplication(sys.argv)
win=Orim()
win.show()
app.exec_()