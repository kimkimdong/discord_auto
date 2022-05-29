import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller  #자동 인스톨
import time
import subprocess  #윈도우서 실행
import datetime
from pytz import timezone
time_now =  datetime.datetime.now(timezone('Asia/Seoul'))


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
        self.pushButton_2.clicked.connect(self.start_discord_auto)
        # self.pushButton_3.clicked.connect(self.quit_chrome)
        
    def start_discord_auto(self): # 작업시작
        with open('./sys/id_lists.txt','r',encoding='utf-8') as f:  #id 가지고 오기/
            ids = f.read().splitlines() 
            
        if len(self.lineEdit.text()) + len(self.lineEdit_2.text()) + len(self.lineEdit_3.text()) == 0 and len(self.lineEdit_4.text()) + len(self.lineEdit_5.text()) != 0:   #  이벤트 가입만 하는경우
            for i in ids[:50]:
                self.open_chrome(i)
                if self.driver.current_url == 'https://discord.com/channels/@me':
                    try:
                        self.event_join()
                        self.driver.close()
                    except:
                        self.driver.close()
                else :
                    self.driver.close()
                    
        elif len(self.lineEdit_4.text()) + len(self.lineEdit_5.text()) == 0 and len(self.lineEdit.text()) + len(self.lineEdit_2.text()) + len(self.lineEdit_3.text()) != 0:   #  서버가입만 하는경우
            for i in ids[:50]:
                self.open_chrome(i)
                if self.driver.current_url == 'https://discord.com/channels/@me':
                    try:
                        self.server_join()
                        self.driver.close()
                    except:
                        self.driver.close()
                else :
                    self.driver.close()

        elif len(self.lineEdit_4.text()) + len(self.lineEdit_5.text()) != 0 and len(self.lineEdit.text()) + len(self.lineEdit_2.text()) + len(self.lineEdit_3.text()) != 0:  # 모두 입력되어있을때
            for i in ids[:50]:
                self.open_chrome(i)
                if self.driver.current_url == 'https://discord.com/channels/@me':
                    try:
                        self.server_join()
                    except:
                        pass
                    try:
                        self.event_join()
                        self.driver.close()
                    except:
                        self.driver.close()
                else :
                    self.driver.close()

    def server_join(self):
        if self.comboBox_2.currentIndex() == 0:
            time.sleep(3)
            self.driver.get(self.lineEdit.text())  #라인에디터1 삽입 초대장
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/section/div/button/div').click()
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div[1]/div/div[1]/button').click() # 완료버튼
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="app-mount"]/div[4]/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div/div[3]/div/label/input').click() #규칙을 읽었으면~~
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="app-mount"]/div[4]/div[2]/div/div/div[2]/div[2]/button').click() # 전송버튼
            self.driver.get(self.lineEdit_2.text())  #라인에디터2 서버가입주소
            time.sleep(3)
            self.driver.find_element_by_xpath(self.lineEdit_3.text()).click()  #라인에디터3 서버가입 클릭
            time.sleep(3)
        elif self.comboBox_2.currentIndex() == 1:
            time.sleep(3)
            self.driver.get(self.lineEdit.text())  #라인에디터1 삽입 초대장
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/section/div/button/div').click()
            time.sleep(3)
            self.driver.get(self.lineEdit_2.text())  #라인에디터2 서버가입주소
            time.sleep(3)
            self.driver.find_element_by_xpath(self.lineEdit_3.text()).click()  #라인에디터3 서버가입 클릭
            time.sleep(3)

    def event_join(self):
        time.sleep(3)
        self.driver.get(self.lineEdit_4.text())  #라인에디터4 이벤트 주소
        time.sleep(3)
        self.driver.find_element_by_xpath(self.lineEdit_5.text()).click()  #라인에디터5 이벤트참여버튼 클릭
        time.sleep(3)

    def create_session(self):  # 세션 생성 
        discord_id=self.comboBox.currentText()
        self.open_chrome(discord_id)

    def open_chrome(self, discord_id):  #크롬 실행
        try:  #  구글로글인 때문에 디버그 모드로 접근하는거 실행
            subprocess.Popen(f'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\discord_data\{discord_id}"')
        except:
            subprocess.Popen(f'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\discord_data\{discord_id}"')
        option = Options()
        option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        option.add_argument("disable-gpu")
        # option.add_argument(f'--user-data-dir=C:\\discord_data\\{discord_id}')   #아이디별로 데이터 만들기
        chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]                      
        try:
            self.driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
        except:
            chromedriver_autoinstaller.install(True)
            self.driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
        self.driver.set_window_size(1400,900)
        self.driver.implicitly_wait(15)
        self.driver.get('https://discord.com/channels/@me')
        if time_now.year == 2022 and time_now.month == 5 :
            pass
        elif time_now.year == 2022 and time_now.month == 6 :
            pass
        elif time_now.year == 2022 and time_now.month == 7 :
            pass
        elif time_now.year == 2022 and time_now.month == 8 :
            pass
        elif time_now.year == 2022 and time_now.month == 9 :
            pass
        elif time_now.year == 2022 and time_now.month == 10 :
            pass
        else:
            self.driver.close()
        
        

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()