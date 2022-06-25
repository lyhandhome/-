from concurrent.futures import ThreadPoolExecutor
import os
import requests
import time

with ThreadPoolExecutor(max_workers=32) as pool:
    start = time.time()
    for i in range(1, 4):
        url = f'https://kuwo.cn/api/www/bang/bang/musicList?bangId=93&pn={i}&rn={i * 30}'
    # print(url)
    headers = {
        'Cookie': '_ga=GA1.2.2106098997.1649896095; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1649896095,1651052126; _gid=GA1.2.1254767668.1651052126; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1651052850; kw_token=FY4W0GV7HYU',
        'csrf': 'FY4W0GV7HYU',
        'Referer': 'https://kuwo.cn/rankList',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    }
    html = requests.get(url, headers=headers)
    # print(html.json())
    # 酷我飙升榜
    # https://kuwo.cn/api/www/bang/bang/musicList?bangId=93&pn=1&rn=30&httpsStatus=1&reqId=f01c8c40-c60d-11ec-8d7c-45805c576a14
    # 酷我新歌榜
    # https://kuwo.cn/api/www/bang/bang/musicList?bangId=17&pn=1&rn=30&httpsStatus=1&reqId=9be78320-c610-11ec-8d7c-45805c576a14
    # 酷我热歌榜
    # https://kuwo.cn/api/www/bang/bang/musicList?bangId=16&pn=1&rn=30&httpsStatus=1&reqId=a11d9690-c610-11ec-8d7c-45805c576a14
    data_list = html.json()['data']['musicList']
    # print(data_list)
    for data in data_list:
        title = data['name']
        id_url = data['rid']
        # print(title, id_url)
        index_url = f'https://kuwo.cn/api/v1/www/music/playUrl?mid={id_url}&type=convent_url'  # VIPconvent_url
        # print(title, index_url)
        v_url = requests.get(url=index_url, headers=headers).json()['data']['url']
        pool.submit(v_url, title)
        print(title, v_url)

        v_content = requests.get(v_url).content
        filename = 'kuwo'
        if not os.path.exists(filename):
            os.makedirs(filename)
        with open('kuwo/{}.mp3'.format(title), mode='ab') as f:
            f.write(v_content)
time.sleep(10)
end = time.time()
print(f'执行时间:{end - start:.3f}秒')
