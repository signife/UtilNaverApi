import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import Keys
import pyperclip

import time
from selenium.webdriver import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

driver.maximize_window()

driver.get('https://play.google.com/store/apps/details?id=com.sampleapp&hl=ko&gl=US')
time.sleep(3)

driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
time.sleep(1)

driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz[2]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/c-wiz[5]/section/header/div/div[2]/button').click()

driver.find_element(By.CLASS_NAME,'fysCi').click()

prev_count = 0
new_count =0
max_count = 100

while True:
    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
    time.sleep(0.5)

    new_count =len(driver.find_elements(By.CLASS_NAME,'h3YV2d'))

    if new_count == prev_count:
        break
    if new_count >= max_count:
        break
    print(new_count)

    prev_count = new_count


data = driver.find_elements(By.CLASS_NAME,'h3YV2d')

data_list = []
for temp in data:
    data_list.append(temp.text.strip())

df = pd.DataFrame({'댓글':data_list})
df.to_csv('배달의민족댓글.csv')


