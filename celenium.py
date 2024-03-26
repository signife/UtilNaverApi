from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time
from selenium.webdriver import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

driver.maximize_window()

driver.get('http://naver.com')
time.sleep(3)

# driver.find_element(By.XPATH,'//*[@id="shortcutArea"]/ul/li[3]/a/span[1]').click()
driver.find_element(By.XPATH,'//*[@id="query"]').send_keys('삼육대학교')
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="query"]').send_keys(Keys.ENTER)

html =driver.page_source
print(html)