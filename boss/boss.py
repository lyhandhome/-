import csv

import requests
from bs4 import BeautifulSoup
from download import get_proxies

for i in range(10,13):
    url = f'https://www.zhipin.com/c100010000/?query=python%E5%AE%9E%E4%B9%A0%E7%94%9F&page={i}'
    headers = {
        'cookie': 'wd_guid=ff62e8a5-476f-4d31-b703-df03810f1335; historyState=state; _9755xjdesxxd_=32; gdxidpyhxdE=s%2BxpU64Sl%2FTD7jHwPB7l%5CO7e%5CWjTBq1w6hjik53yxR6vQRkDlUbeWN58jxc2WGOcEfw%5CGtATKk%2FOX%5CPHthdzIymfOTqUJ4s09G%5CGDDKD0I24U92%2FpjTtSwtws5hK%5CBBGXGxJS6t7EKrQTDW6RgeJCMK24b0jmJzgrj14c%2Bo542UxRTRE%3A1651991333936; YD00951578218230%3AWM_NI=6gQTXuZOoRBcYj1QRo3WycutEGmzYvulXaXUhWr7dAdipnbltZG3NqqmpKYp%2FBQOaLZmK6SRj8Cs88izWV%2FFLi5oU9GF007%2F2qJ%2BMgthLGkElcdNPJj8FmeQEH1an%2FLhamE%3D; YD00951578218230%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eea2ea3db4ba8f8eb159f1eb8eb6c84e879b8fb1c14e8af083bbcf6a8199a192d82af0fea7c3b92af6b99fb5db7f9a91a1b3c1699bb6ffb2d165f189b784f8808799a39bdc7eb7b49882db5fac89bed8e74ba8b7c08fe168b88689d4cd7bb3b3c0acdc7ced9e9fb0e4489ab385d7d25aaae88d94bb34aba699b7ae4e90b7fb90d833859a00d1b625f2af86ccd06db8b884a8ea4fb0bdacafd342aae88a8ee85b8798ff82ed2590b8af8ec837e2a3; YD00951578218230%3AWM_TID=I3ZMu6l1O%2FZAVABQUUKQVYxNceKGH4rR; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1651218270,1651990017,1651998051,1652055131; lastCity=100010000; __l=l=%2Fwww.zhipin.com%2Fjob_detail%2F70da416ffc9b13341nV53N68FFtX.html&r=&g=&s=3&friend_source=0&s=3&friend_source=0; __c=1652055130; __a=86176663.1647696108.1651998051.1652055130.251.13.36.106; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1652068532; __zp_stoken__=d732dbmRnFXFmYW4Celd6MRJiXAhibS5DA3tsQgEkcQNLAkkPd2sxfwQCDGdTeDNjGwxyUyZhDVwVN1BNRUAmYRENM1gyRyhSQHFCXgl1Pw5QanRtdVYDW1k7FlY2ZBJ%2BOQxWBnBVLgQfbRsJCjJoDygLBXgUJEVLKGFhFAIDVkV%2BUDIITGg4F2QCOh10XSAARAZUfjhHfA%3D%3D',
        'referer': 'https://www.zhipin.com/c100010000-p100109/?query=%E7%88%AC%E8%99%AB%E5%AE%9E%E4%B9%A0%E7%94%9F&page=9&ka=page-9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    }
    html = requests.get(url, headers=headers, proxies=get_proxies()).text
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    data_list = soup.select('.job-list > ul > li')
    # print(data_list)

    for d in data_list:

        # 获取工作名称
        title = d.select_one('span.job-name').text
        print(title)

        # 获取企业名称
        company = d.select_one('h3.name a').text
        print(company)

        # 获取技术能力
        art = d.select_one('div.tags').text.split()[0]
        print(art)

        # 获取薪资
        salary = d.select_one('span.red').text
        print(salary)

        # 获取实习时长
        time = d.select_one('.job-limit.clearfix > p').text
        print(time)

        # 获取福利
        try:
            welfare = d.select_one('.info-desc').text
            print(welfare)
        except Exception as e:
            welfare = '无'
            print(welfare)

        #获取工作地点
        area = d.select_one('span.job-area').text
        print(area)
        # 获取这一工作详细页的链接
        index_url = d.select_one('.job-name a').attrs['href']
        v_url = 'https://www.zhipin.com' + index_url
        print(v_url)

        with open('python实习.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_write = csv.writer(f)
            csv_write.writerow([title, company, area, time, art, welfare, salary, v_url])

    # res = requests.get(url=v_url, headers=headers, proxies=get_proxies()).text
    # # print(res)
    # soup1 = BeautifulSoup(res, 'lxml')
    #
    # # 获取工作内容
    # try:
    #     data = soup1.select_one('div.text')
    #     print(data)
    # except Exception as e:
    #     data = '无'
    #     print(data)
