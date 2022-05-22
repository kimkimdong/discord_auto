import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller  #자동 인스톨



form_class = uic.loadUiType("./sys/discord_auto.ui")[0]
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        with open('./sys/id_lists.txt','r',encoding='utf-8') as f:
            id_lists = f.read().splitlines() # 개행연산자 빼고 리스트가 됨
        for i in id_lists:
            self.comboBox.addItem(i)
            
        self.pushButton.clicked.connect(self.create_session)
    def create_session(self):  # 세션 생성 
        discord_id=self.comboBox.currentText()
        option = Options()
        option.add_argument("disable-gpu")
        option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4577.63 Safari/537.36")
        option.add_argument(f'--user-data-dir=C:\\discord_data\\{discord_id}')   #아이디별로 데이터 만들기
        chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]                      
        try:
            driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
        except:
            chromedriver_autoinstaller.install(True)
            driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
        driver.get('https://discord.com/channels/@me')
# 내용
#app-mount > div.app-3xd6d0 > div > div.leftSplit-hm3715.nonEmbeddedLeftSplit-1DjcEq > div > div > div > section > div > button
#app-mount > div.app-3xd6d0 > div > div.leftSplit-hm3715.nonEmbeddedLeftSplit-1DjcEq > div > div > div > section > div > button
#app-mount > div.app-3xd6d0 > div > div.leftSplit-hm3715.nonEmbeddedLeftSplit-1DjcEq > div > div > div > section > div > button
#app-mount > div.app-3xd6d0 > div > div.leftSplit-hm3715.nonEmbeddedLeftSplit-1DjcEq > div > div > div > section > div > button
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()