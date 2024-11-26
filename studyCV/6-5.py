from PyQt5.QtWidgets import *
import cv2 as cv
import numpy as np
import winsound
import sys

# Panorama 클래스 선언
class Panorama(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle('파노라마 영상')
        self.setGeometry(200,200,700,200)
        
        # 버튼 5개, 레이블 1개 생성
        collectButton=QPushButton('영상 수집',self)
        self.showButton=QPushButton('영상 보기',self) 
        self.stitchButton=QPushButton('봉합',self) 
        self.saveButton=QPushButton('저장',self)
        quitButton=QPushButton('나가기',self)
        self.label=QLabel('환영합니다!',self)
        
        collectButton.setGeometry(10,25,100,30)
        self.showButton.setGeometry(110,25,100,30) 
        self.stitchButton.setGeometry(210,25,100,30) 
        self.saveButton.setGeometry(310,25,100,30)
        quitButton.setGeometry(450,25,100,30) 
        self.label.setGeometry(10,70,600,170)

        # 나머지 3개 버튼 비활성화
        self.showButton.setEnabled(False) 
        self.stitchButton.setEnabled(False) 
        self.saveButton.setEnabled(False)
        
        # 버튼 클릭 시 수행할 콜백함수 등록
        collectButton.clicked.connect(self.collectFunction)
        self.showButton.clicked.connect(self.showFunction)       
        self.stitchButton.clicked.connect(self.stitchFunction) 
        self.saveButton.clicked.connect(self.saveFunction)   
        quitButton.clicked.connect(self.quitFunction)        

    ## 콜백함수 선언
    # <영상 수집> 버튼 클릭 시 실행
    def collectFunction(self):
        # <영상 수집>버튼 실행 즉시 <영상 보기>,<봉합>,<저장> 버튼 비활성화
        self.showButton.setEnabled(False) 
        self.stitchButton.setEnabled(False) 
        self.saveButton.setEnabled(False)
        self.label.setText('c를 여러 번 눌러 수집하고 끝나면 q를 눌러 비디오를 끕니다.')
        
        self.cap=cv.VideoCapture(0,cv.CAP_DSHOW)
        if not self.cap.isOpened(): sys.exit('카메라 연결 실패')
        
        self.imgs=[]   
        while True:
            ret,frame=self.cap.read()  
            if not ret: break
            
            cv.imshow('video display', frame)
            
            key=cv.waitKey(1)
            if key==ord('c'):   # c 누르면 영상 저장            
                self.imgs.append(frame) 
            elif key==ord('q'): # q 누르면 비디오 연결 및 윈도우 창 종료
                self.cap.release() 
                cv.destroyWindow('video display')            
                break 
        
        if len(self.imgs)>=2:      # 수집한 영상이 2장 이상이면 나머지 3개 버튼 활성화
            self.showButton.setEnabled(True) 
            self.stitchButton.setEnabled(True) 
            self.saveButton.setEnabled(True)        

    # <영상 보기> 버튼 클릭 시 실행                
    def showFunction(self):
        self.label.setText('수집된 영상은 '+str(len(self.imgs))+'장 입니다.')   # 수집된 영상 수 레이블에 표시
        stack=cv.resize(self.imgs[0],dsize=(0,0),fx=0.25,fy=0.25)   # 수집된 영상 0.25배로 변환
        for i in range(1,len(self.imgs)):   # 수집한 영상들 나열하기 (하나씩 stack에 저장)
            stack=np.hstack((stack,cv.resize(self.imgs[i],dsize=(0,0),fx=0.25,fy=0.25))) 
        cv.imshow('Image collection',stack) # stack에 저장된 이미지 띄우기

    # <봉합> 버튼 클릭 시 실행    
    def stitchFunction(self):
        stitcher=cv.Stitcher_create()   # 영상 봉합에 쓸 stitcher 객체 생성
        status,self.img_stitched=stitcher.stitch(self.imgs) # stitch 함수로 봉합 시도, stitch(수집한 영상 객체)
        if status==cv.STITCHER_OK:  # 봉합 성공
            cv.imshow('Image stitched panorama',self.img_stitched)  # 새 윈도우에 파노라마 영상 디스플레이  
        else:   # 봉합 실패
            winsound.Beep(3000,500) # 비프음 출력       
            self.label.setText('파노라마 제작에 실패했습니다. 다시 시도하세요.')    

    # <저장> 버튼 클릭 시 실행        
    def saveFunction(self):
        fname=QFileDialog.getSaveFileName(self,'파일 저장','./')
        cv.imwrite(fname[0],self.img_stitched)

    # <나가기> 버튼 클릭 시 실행    
    def quitFunction(self): 
        self.cap.release() 
        cv.destroyAllWindows()  
        self.close()

app=QApplication(sys.argv) 
win=Panorama() 
win.show()
app.exec_()

