import cv2 as cv
import numpy as np
from PyQt5.QtWidgets import *
import sys    
    
class SpecialEffect(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('사진 특수 효과')
        self.setGeometry(200,200,800,200)
       
        # 버튼 7개,레이블 1개,콤보박스 1개 생성
        pictureButton=QPushButton('사진 읽기',self)
        embossButton=QPushButton('엠보싱',self)
        cartoonButton=QPushButton('카툰',self)
        sketchButton=QPushButton('연필 스케치',self)
        oilButton=QPushButton('유화',self)
        saveButton=QPushButton('저장하기',self) 
        self.pickCombo=QComboBox(self)     
        self.pickCombo.addItems(['엠보싱','카툰','연필 스케치(명암)','연필 스케치(컬러)','유화'])
        quitButton=QPushButton('나가기',self)        
        self.label=QLabel('환영합니다!',self)
        
        # 버튼, 레이블, 콤보박스 위젯의 위치와 크기를 지정
        pictureButton.setGeometry(10,10,100,30)
        embossButton.setGeometry(110,10,100,30)
        cartoonButton.setGeometry(210,10,100,30)
        sketchButton.setGeometry(310,10,100,30)
        oilButton.setGeometry(410,10,100,30)  
        saveButton.setGeometry(510,10,100,30)
        self.pickCombo.setGeometry(510,40,110,30)                  
        quitButton.setGeometry(620,10,100,30)
        self.label.setGeometry(10,40,500,170)
        
        # 버튼을 클릭했을 때 수행할 콜백 함수 등록
        pictureButton.clicked.connect(self.pictureOpenFunction)
        embossButton.clicked.connect(self.embossFunction) 
        cartoonButton.clicked.connect(self.cartoonFunction)
        sketchButton.clicked.connect(self.sketchFunction)
        oilButton.clicked.connect(self.oilFunction) 
        saveButton.clicked.connect(self.saveFunction)    
        quitButton.clicked.connect(self.quitFunction)

    # <사진 읽기> 버튼 클릭 시 실행
    def pictureOpenFunction(self):
        # 폴더에서 사진 파일을 브라우징하여 선택하고 읽어오기
        fname=QFileDialog.getOpenFileName(self,'사진 읽기','./')
        self.img=cv.imread(fname[0])    
        if self.img is None: sys.exit('파일을 찾을 수 없습니다.')  
        
        cv.imshow('Painting',self.img)         

    # <엠보싱> 버튼 클릭 시 실행
    def embossFunction(self):
        femboss=np.array([[-1.0, 0.0, 0.0],[0.0, 0.0, 0.0],[0.0, 0.0, 1.0]])    # 엠보싱 필터 정의
        # 명암 영상으로 변환하 고 컨볼루션을 적용
        gray=cv.cvtColor(self.img,cv.COLOR_BGR2GRAY)    
        gray16=np.int16(gray)
        self.emboss=np.uint8(np.clip(cv.filter2D(gray16,-1,femboss)+128,0,255))
        
        cv.imshow('Emboss',self.emboss)
    
    # <카툰> 버튼 클릭 시 실행
    def cartoonFunction(self):
        self.cartoon=cv.stylization(self.img,sigma_s=60,sigma_r=0.45)   # 매개변수는 기본값으로 설정
        cv.imshow('Cartoon',self.cartoon) 
    
    # <연필 스케치> 버튼 클릭 시 실행
    def sketchFunction(self):
        self.sketch_gray,self.sketch_color=cv.pencilSketch(self.img,sigma_s=60,sigma_r=0.07,shade_factor=0.02)
        cv.imshow('Pencil sketch(gray)',self.sketch_gray)
        cv.imshow('Pencil sketch(color)',self.sketch_color)

    # <유화> 버튼 클릭 시 실행
    def oilFunction(self):
        self.oil=cv.xphoto.oilPainting(self.img,10,1,cv.COLOR_BGR2Lab)
        cv.imshow('Oil painting',self.oil) 
                           
    def saveFunction(self):      
        fname=QFileDialog.getSaveFileName(self,'파일 저장','./')
        
        i=self.pickCombo.currentIndex()
        if i==0: cv.imwrite(fname[0],self.emboss)
        elif i==1: cv.imwrite(fname[0],self.cartoon)
        elif i==2: cv.imwrite(fname[0],self.sketch_gray)
        elif i==3: cv.imwrite(fname[0],self.sketch_color)
        elif i==4: cv.imwrite(fname[0],self.oil)
                        
    def quitFunction(self):
        cv.destroyAllWindows()        
        self.close()
                
app=QApplication(sys.argv) 
win=SpecialEffect() 
win.show()
app.exec_()
