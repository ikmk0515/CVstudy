from PyQt5.QtWidgets import *
import sys
import winsound

class BeepSound(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('삑 소리 내기') #윈도우 이름과 위치 지정
        self.setGeometry(200,200,600,150)   
        
        # 버튼 생성
        shortBeepButton=QPushButton('짧게 삑',self)
        longBeepButton=QPushButton('길게 삑',self)
        quitButton=QPushButton('나가기',self)
        msgButton=QPushButton('띠로롱',self)
        self.label=QLabel('환영합니다!',self)

        # 버튼 위치와 크기 지정
        shortBeepButton.setGeometry(10,10,100,30)
        longBeepButton.setGeometry(110,10,100,30)
        quitButton.setGeometry(210,10,100,30)
        msgButton.setGeometry(410,10,100,100)
        self.label.setGeometry(10,40,400,70)

        # 콜백 함수 지정
        shortBeepButton.clicked.connect(self.shortBeepFunction)
        longBeepButton.clicked.connect(self.longBeepFunction)
        quitButton.clicked.connect(self.quitFuction)
        msgButton.clicked.connect(self.msgFunction)

    def shortBeepFunction(self):
        self.label.setText('주파수 1000으로 0.5초 동안 삑 소리를 냅니다.')
        winsound.Beep(1000,500)
    
    def longBeepFunction(self):
        self.label.setText('주파수 1000으로 3초 동안 삑 소리를 냅니다.')
        winsound.Beep(1000,3000)

    def quitFuction(self):
        self.close()

    def msgFunction(self):
        self.label.setText("뾰로롱")
        winsound.MessageBeep()
    
app=QApplication(sys.argv)
win=BeepSound()
win.show()
app.exec_()