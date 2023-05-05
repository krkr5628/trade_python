# from PyQt5.QtWidgets import * : 파이썬 위젯, 클릭-버튼-진행바 등
# PyQt5.QAxContainer import * : 키움증권의 클레스를 사용할 수 있게 함
# from PyQt5Singleton import Singleton : PyQt5Singleton Singleton 함수를 가져옴
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5Singleton import Singleton


# QMainWindow : PyQt5에서 윈도우 생성시 필요한 함수
# class Kiwoom(QWidget, metaclass=Singleton) : Kiwoom 클래스는 metaclass=Singleton에 의해 생성된 객체, 메타클래스에 의해 인스턴스화 됨
# 메타클래스 : 클래스를 관리하는 클래스, 클래스라는 객체를 만들기 위한 클래스
# def __init__(self, parent=None, **kwargs) : Main class의 self를 초기화 한다.
# parent=None : 특별히 parent를 명시하지 않아도 됨다는 의미. Kiwoom은 이미 Singletom의 인스턴스이기 때문
# 키움에서 제공하는 함수를 사용하기 위해서 반드시 self.kiwoom을 사용
class Kiwoom(QWidget, metaclass=Singleton):
    def __init__(self, parent=None, **kwargs):
        print("로그인 프로그램을 실행합니다.")
        super().__init__(parent, **kwargs)
        ################ 로그인 관련 정보
        self.kiwoom = QAxWidget('KHOPENAPI.KHOpenAPICtrl.1')  # CLSID
