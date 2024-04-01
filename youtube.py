import sys
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd


# 크롬 웹드라이버 설치 및 설정
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window() # 브라우저 전체화면

# 설정
keyword = '연세대학교' # 검색할 제목
count = -1 # 스크래핑할 댓글 개수. (값을 -1로 하면 한계까지 수집)
save_interver = 2

# 크롬 열기 및 주소입력
driver.get('https://www.youtube.com/results?search_query=' + keyword)
driver.implicitly_wait(5)
time.sleep(2)

# 영상 선택
thumbnails = driver.find_elements(By.XPATH, '//*[@id="dismissible"]/ytd-thumbnail')
driver.implicitly_wait(5)
time.sleep(2)

for temp in thumbnails:
    print('==========1')
    time.sleep(5)
    temp.click()
    save_interver_count = 0
    while True:
        # 스크롤 전 현재높이 저장
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        print('new_height:', new_height)
        time.sleep(1)  # 1초 대기

        # while문 멈출지 체크

        if count == -1:  # 페이지 끝까지 while문 돌리기
            # 페이지 끝까지 스크롤 내리기
            driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.END)
            time.sleep(1)  # 1초 대기

            # 스크롤 후 현재높이 저장
            last_height = driver.execute_script("return document.documentElement.scrollHeight")
            time.sleep(1)  # 1초 대기

            # 페이지 끝까지 스크롤 했는지 판단
            if new_height == last_height:  # if(이전 스크롤 높이 = 현재 스크롤 높이) 마지막 페이지라 판단. while문 탈출
                  # save_interver 만큼 스크롤을 내렸다면
                    print('111')
                    save_interver_count = 0  # 초기화

                    # 페이지 읽기
                    html = driver.page_source
                    soup = BeautifulSoup(html, 'html.parser')
                    time.sleep(1)

                    # 댓글 구역 추출하기
                    comments_sections = soup.find_all('ytd-comment-thread-renderer', class_='ytd-item-section-renderer')

                    # 저장하기
                    username = []
                    usercomment = []
                    print('222')
                    print(len(comments_sections))
                    for item in comments_sections:
                        try:
                            a = item.find('yt-formatted-string', id='text').get_text()
                            b = item.find('yt-formatted-string', id='content-text').get_text()
                        except:
                            a = item.find('a', id='author-text').get_text().strip()
                            b = item.find('yt-formatted-string', id='content-text').get_text()
                        username.append(a)
                        usercomment.append(b)
                    data = pd.DataFrame({'user name': username, 'user comment': usercomment})
                    data.to_csv('youtube_data.csv', index=False,mode='a')
                    print('csv 저장 완료')
                    driver.back()
                    time.sleep(2)
                    break
        else:
            # 페이지 읽기
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            time.sleep(1)

            # 댓글 구역 추출하기
            comments_sections = soup.find_all('ytd-comment-thread-renderer', class_='ytd-item-section-renderer')

            if len(comments_sections) < count:  # 수집하려는 개수보다 확보된 댓글이 많다면
                # 페이지 끝까지 스크롤 내리기
                driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.END)
                time.sleep(1)  # 1초 대기

                # 스크롤 후 현재높이 저장
                last_height = driver.execute_script("return document.documentElement.scrollHeight")
                print('last_height:', last_height)
                time.sleep(1)  # 1초 대기

                # 페이지 끝까지 스크롤 했는지 판단
                if new_height == last_height:  # if(이전 스크롤 높이 == 현재 스크롤 높이) 마지막 페이지라 판단. while문 탈출
                    break
            else:
                print(f'{count}만큼 댓글 확보 완료')
                del comments_sections[count:]  # 댓글 구역에서 count 보다 초과된 댓글 삭제
                break


    print('==========end')
    # driver.back()



