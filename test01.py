from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller  #자동 인스톨
import subprocess  #윈도우서 실행
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
# try:  #  구글로글인 때문에 디버그 모드로 접근하는거 실행
#     subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\discord_data\ruslankolodkin.1987@rambler.ru"')
# except:
#     subprocess.Popen(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\discord_data\ruslankolodkin.1987@rambler.ru"')
option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
option.add_argument("disable-gpu")
# option.add_argument(f'--user-data-dir=C:\\discord_data\\{discord_id}')   #아이디별로 데이터 만들기
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]                      
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
driver.set_window_size(1400,900)
driver.implicitly_wait(15)
driver.get('https://discord.com/channels/912314917393154128/974523774412161034')
time.sleep(1)
ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
time.sleep(1)
ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
time.sleep(1)
ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
time.sleep(1)
ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
time.sleep(1)
ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
time.sleep(1)
ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
print(driver.page_source)