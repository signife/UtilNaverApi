from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import Keys
import pyperclip

def naverlogin(idata,pdata):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach',True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

    driver.maximize_window()

    driver.get('http://naver.com')
    time.sleep(3)

    driver.find_element(By.CLASS_NAME,'MyView-module__link_login___HpHMW').click()
    time.sleep(5)

    naverid = idata
    naverpw = pdata

    pyperclip.copy(naverid)

    driver.find_element(By.ID,'id').click()
    pyperclip.copy(naverid)
    driver.find_element(By.ID,'id').send_keys(Keys.CONTROL,'v')

    time.sleep(3)

    driver.find_element(By.ID,'pw').click()
    pyperclip.copy(naverpw)
    driver.find_element(By.ID,'pw').send_keys(Keys.CONTROL,'v')
    time.sleep(1)

    driver.find_element(By.CLASS_NAME,'btn_login').click()

