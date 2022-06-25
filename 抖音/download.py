import os
import random
import time

import requests


def download(v_url):
    filename = '哲学'
    if not os.path.exists(filename):
        os.makedirs(filename)
    v_content = requests.get(v_url).content
    with open('哲学/movie_{:04}.mp4'.format(random.randint(0, 200)), mode='ab')as f:
    # with open('小姐姐1/movie_{:02}.mp4'.format(x), mode='ab') as f:

        f.write(v_content)


def download1(v_url, title):
    filename = '哲学'
    if not os.path.exists(filename):
        os.makedirs(filename)
    v_content = requests.get(v_url).content
    with open('哲学/{}.mp4'.format(title), mode='ab')as f:
    # with open('小姐姐1/movie_{:02}.mp4'.format(x), mode='ab') as f:

        f.write(v_content)


def drop_down():
    # 执行页面滚动的操作  JavaScript
    for i in range(1, 100, 4):  # 1 3 5 7 9 在你不断的下拉过程中， 页面高度也会变的
        time.sleep(1)
        j = i / 9  # 1/9 3/9 5/9 7/9
        # document.documentElement.scrollTop 指定滚动条的位置
        # document.documentElement.scrollHeight 获取浏览器页面的最大高度
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        # driver.execute_script(js)
# x = [i for i in range(104)]
# print(x)
