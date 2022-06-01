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
driver.get('https://discord.com/invite/camochameleonclub')
# marginTop40-Q4o1tS button-1cRKG6 button-f2h6uQ lookFilled-yCfaCM colorBrand-I6CyqQ sizeLarge-3mScP9 fullWidth-fJIsjq grow-2sR_-F
# marginTop40-Q4o1tS button-1cRKG6 button-f2h6uQ lookFilled-yCfaCM colorBrand-I6CyqQ sizeLarge-3mScP9 fullWidth-fJIsjq grow-2sR_-F
time.sleep(2)
# driver.find_element_by_css_selector('button.marginTop?40-Q4o1tS.button-1cRKG6.button-f2h6uQ.lookFilled-yCfaCM.colorBrand-I6CyqQ.sizeLarge-3mScP9.fullWidth-fJIsjq.grow-2sR_-F')

while True:
    try:
        body = driver.find_element_by_css_selector('body')
    except:
        driver.refresh()
        time.sleep(1)
        
driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/div/div/section/div/button')