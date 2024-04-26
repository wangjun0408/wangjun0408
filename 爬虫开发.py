###爬取网站的所有
#网址：https://www.acgndog.com/（次元狗动漫）
# https://www.acgndog.com/37990.html 2023 七月动漫排行表
'''
在这个示例中，我们首先发送了一个 GET 请求来获取指定网址的内容。
然后使用 BeautifulSoup 解析 HTML 内容，并找到包含动漫列表的容器。
接着，我们提取每部动漫的信息，并打印出动漫的名称。你也可以根据需要提取其他信息，比如动漫的介绍、评分等。
'''
import requests
from bs4 import BeautifulSoup

def scrape_anime_list(url):
    # 发送 GET 请求获取网页内容
    response = requests.get(url)
    # 检查响应是否成功
    if response.status_code == 200:
        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(response.content,'html.parser')
        # 找到动漫列表的容器
        anime_container = soup.find('div', class_='zw-novellist')
        #调试输出
        print("Anime container:", anime_container)
        if anime_container:
            # 提取每部动漫的信息
            anime_list = anime_container.find_all('li')

             # 遍历动漫列表并打印信息
            for anime in anime_list:
                 # 获取动漫名称
                  anime_name = anime.find('a').text.strip()
                  print(anime_name)


            # 获取动漫的其他信息，比如介绍、评分等，根据需要自行提取
        else:
            print("Failed to find anime container.")
    else:
        print("Failed to retrieve anime list. Status code:", response.status_code)

# 要爬取的网站 URL
url = "https://www.acgndog.com/37990.html"

# 调用函数来爬取动漫列表
scrape_anime_list(url)







