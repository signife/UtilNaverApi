import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

driver.maximize_window()
driver.get('https://www.instagram.com/')
time.sleep(3)


driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('heypythonai@gmail.com')
driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('!123456')
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]').click()
time.sleep(5)
driver.get('https://www.instagram.com/explore/tags/앱테크')
time.sleep(10)
driver.find_elements(By.CLASS_NAME,'_aagw')[0].click()
time.sleep(3)

result = []
while len(result) < 10: #3개의 댓글
    while True: #댓글더읽기버튼 클릭
        driver.find_element(By.CLASS_NAME,'_a9z6').click()
        driver.find_element(By.TAG_NAME,'body').send_keys(Keys.END)#스크롤은 바디에
        time.sleep(2)


        plus_button = driver.find_elements(By.XPATH,'//*[@aria-label="댓글 더 읽어들이기" and @class="x1lliihq x1n2onr6 x5n08af"]')
        print(len(plus_button))
        if len(plus_button) > 0:
            print("버튼찾음")
            plus_button[-1].click()
            time.sleep(5)
        else:
            break
    try: #댓글이 있는경우
        comments = driver.find_elements(By.CLASS_NAME,'_a9zs')

        comments_list = []
        for temp in comments:
            print(temp.text)
            comments_list.append(temp.text)

        result.append(comments_list)
        time.sleep(1)

        # next_btn = driver.find_elements(By.XPATH,'//*[@aria-label="다음" and @class="x1lliihq x1n2onr6"]')
        #
        # if len(next_btn)>0:
        #     next_btn[-1].click()

        next_btn = driver.find_elements(By.XPATH,'//*[@aria-label="다음"]')
        if len(next_btn)>0:
            next_btn[0].click() #사진 클릭안되게 -1대신 0
        else:
            break
    except: #댓글이 없는 경우
        next_btn = driver.find_elements(By.XPATH,'//*[@aria-label="다음"]')
        if len(next_btn)>0:
            next_btn[0].click() #사진 클릭안되게 -1대신 0
        else:
            break
#csv 저장





