## 使用python中的requests库来获取网页的内容，然后使用BeautifulSoup库
## 来解析HTMl文档，并提取文字和图片

import requests
from bs4 import BeautifulSoup
import os

# 定义爬取网页的函数
def crawl_iqiyi(url):
    # 发送请求，获取网页内容
    response = requests.get('https://www.iqiyi.com/')

    # 确认请求成功
    if response.status_code == 200:
        # 使用beautifulSoup解析网页内容
        soup = BeautifulSoup(response.text,'html.parser')

        # 提取网页标题
        title = soup.title.string
        print("网页标题:",title)
        
        #创建目录保存图片
        if not os.path.exists(title):
            os.makedirs(title)

        #提取文字
        texts = soup.find_all('p') #假设文字都在<p>标签中
        for idx, text in enumerate(texts):
            print("文字{}:{}".format(idx + 1, text.get_text()))

        #提取图片链接
        imgs = soup.find_all('img')
        for idx,img in enumerate(imgs):
            img_url = img['src']
        
        #下载图片
        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            img_name = os.path.join(title,'img_{}.jpg',format(idx+1))
            with open(img_name,'wb')as img_file:
                img_file.write(img_response.content)
                print("已下载图片：",img_name)
        else:
            print("无法下载图片：",img_url)
                  
    else:
        print("请求失败") 



            