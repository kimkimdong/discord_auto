from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller  #자동 인스톨
import subprocess  #윈도우서 실행

try:  #  구글로글인 때문에 디버그 모드로 접근하는거 실행
    subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\discord_data\modoc_blinov_32@autorambler.ru"') # 디버거 크롬 구동
except:


    subprocess.Popen(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\discord_data\modoc_blinov_32@autorambler.ru"')

option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]                      #디버그 모드 빼고 자동로그인만 도 가능
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
driver.set_window_size(1400,900)
driver.implicitly_wait(10)
driver.get('https://www.naver.com/')