from selenium import webdriver
import time, requests, re, os
from random import randint


class BlogCommentVolum(object):

    def __init__(self):
        path = os.getcwd()
        self.dr = webdriver.Chrome(path+'/chromedriver.exe')

    def get_request(self, url):
        '''给出url,获取网页回应'''
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
        cookie = 'UM_distinctid=160341f651719b-0a28626b313549-6010107f-100200-160341f651a254; bdshare_firstime=1512702967361; JSESSIONID=99a0f24f-c2ed-4514-9667-665c8f97a2eb; notActiveUserIDPC=24055652; CNZZDATA1574657=cnzz_eid%3D807145515-1512698342-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1521635184; Hm_lvt_cc6a63a887a7d811c92b7cc41c441837=1521637252; tgbuser=1620381; tgbpwd=4048A6FAEF4cc5s8gs5k1ynwsh; Hm_lpvt_cc6a63a887a7d811c92b7cc41c441837=1521637544'
        headers = {
            "User-Agent": user_agent,
            "cookie": cookie
        }
        response = requests.get(url, headers=headers)
        response = response.text
        return response

    def get_url(self, response):
        """获取所有博客地址"""
        pattern = re.compile(r'<div class="article-list">(.*?)</main>', re.S)
        item = pattern.findall(str(response))
        pattern1 = re.compile(r'class="content".*?<a href="(.*?)".*?target="_blank">', re.S)
        urls = pattern1.findall(str(item))
        target_url = []
        for url in urls:
            if 'Luzaofa' not in url:
                pass
            else:
                target_url.append(url)
        return target_url

    def Main(self, URL, Page):
        """点击链接进行访问"""
        self.dr.implicitly_wait(1)
        for page_ in range(1, Page + 1):
            print(f'正在访问第{page_}页！')
            url = URL.format(page=page_)
            response = self.get_request(url)
            blog_urls = self.get_url(response)
            for url in blog_urls:
                # num = randint(1, 10)
                num = 1
                print(f'即将对其发起 {num} 次访问请求：{url}')
                for T in range(num):
                    self.dr.get(url)
                    time.sleep(randint(1, 10))


if __name__ == '__main__':

    BlogCommentVolum = BlogCommentVolum()
    url = 'https://blog.csdn.net/luzaofa/article/list/{page}'
    page = 3
    while True:
        BlogCommentVolum.Main(url, page)
