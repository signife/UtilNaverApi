import os
import sys
import urllib.request
import json
import requests
import numpy as np
import pandas as pd
from tqdm import tqdm

from bs4 import BeautifulSoup as bs

def naver_blog(sdata):
    client_id = "4Gsl7IpgS8vEMmvfODda"
    client_secret = "A3A_TqKzpW"
    encText = urllib.parse.quote(sdata)

    link_list = []
    title_list = []

    for item in range(1, 1001, 100):

        url = "https://openapi.naver.com/v1/search/blog?query=" + encText + '&display=100' + '&start={0}'.format(
            item)  # JSON 결과

        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request)

        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            blogdata = json.loads(response_body)

            for blog_temp in blogdata['items']:
                # ----중요----#
                link = blog_temp['link'].replace('https://blog', 'https://m.blog')
                title = blog_temp['title']

                if 'naver' in link:
                    link_list.append(link)
                    title_list.append(title)

        else:
            print("Error Code:" + rescode)

    df = pd.DataFrame({'제목': title_list, '주소': link_list})
    # df.to_csv('삼육대학교.csv')

    # count = 0
    blog_text_list = []
    for temp in tqdm(df['주소']):
        try:
            # print(temp)
            html = requests.get(temp)
            soup = bs(html.text, 'html.parser')
            result = soup.find_all('span', class_='se-fs-')
            # print(result)

            # print(count)
            # count += 1

            blog_text = ''
            for item in result:
                blog_text += item.text

            blog_text_list.append(blog_text)
        except:
            blog_text_list.append('')

    print('총블로그수:',len(blog_text_list))
    df['내용'] = blog_text_list

    df.to_csv('팝콘.csv')

naver_blog('영화관+팝콘+포장')


