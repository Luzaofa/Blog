from selenium import webdriver
import time, os
from random import randint


class BlogCommentVolum(object):

    def __init__(self):
        self.path = os.getcwd()
        self.dr = webdriver.Chrome(self.path + '/chromedriver.exe')

    def Main(self):
        """点击链接进行访问"""
        self.dr.implicitly_wait(1)
        blog_urls = open(self.path + '/blog_url.txt').readlines()
        for url in blog_urls:
            # num = randint(1, 10)
            num = 1
            print(f'即将对其发起 {num} 次访问请求：{url}')
            for T in range(num):
                self.dr.get(url)
                time.sleep(randint(1, 10))


if __name__ == '__main__':

    BlogCommentVolum = BlogCommentVolum()
    while True:
        BlogCommentVolum.Main()
