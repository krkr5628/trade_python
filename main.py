# sys :system specific parameter and functions를 가져옴, 스크립트 관리
# from PyQt5.QtWidgets import * : 파이썬 위젯
# from PyQt5 import uic : ui를 class 형태로 변환
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


# 0 : 앞으로 만들 UI_MAINWindow 클래스
# 1 : 위젯의 MainWindow
form_class = uic.loadUiType("main_windows.ui")[0]


# QMainWindow(윈도우 생성), QWidget(버튼), form_class(ui)
# __init__ : 아래에 사용할 self가 붙은 변수들을 초기화하는 역할
# 별표(*) : 정의하지 않는 일반 인자를 함수 def에 보낼때 사용, 1 2 3 => 1 2 3
# 쌍별표(**) : 키워드파라미터 인자를 def에 보낼때 사용, x = 1 => (x,1)
# super(Login, self).__init__(*args, **kwargs) : 부모 클래스(Login 클래스)를 찾는 과정
# form_class.__init__(self) : form_class 초기화
# setupui : 파이썬 내장 함수, ui와 코드간 연결
class Login(QMainWindow, QWidget, form_class):
    def __init__(self, *args, **kwargs):
        print("Login Machine 실행합니다.")
        super(Login, self).__init__(*args, **kwargs)
        form_class.__init__(self)
        self.setUI()

    def setUI(self):
        self.setupUi(self)


# __name__=='__main__' : 이름이 main이라면 아래의 코드 실행
# app = QApplication(sys.argv) : 컴퓨터에 무엇을 실행시켜야 하는지 알려줌, QApplication 실행
# sys.argv : 현재 작업중인 스크립트의 절대 주소
# CH = Login() : 코드 실행
# CH.show() : 코드 보여줌
# app.exec_() : : 프로그램이 종료되지 않게 무한반복 시키는 함수
# QApplication(sys.argv)와 app.exec_()는 이벤트 루프를 만드는 함수, 사이의 코드는 무한 반복 실행
if __name__=='__main__':
    app = QApplication(sys.argv)
    CH = Login()
    CH.show()
    app.exec_()