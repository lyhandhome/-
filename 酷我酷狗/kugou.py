from concurrent.futures.thread import ThreadPoolExecutor
import requests
import os
import re
import time
with ThreadPoolExecutor(max_workers=32) as pool:
    start = time.time()
    ch = ['1-6666', '1-8888', '1-52144', '1-52767', '1-24971', '1-21101', '1-49224']
    for c in ch:
        url = f'https://www.kugou.com/yy/rank/home/{c}.html?from=rank'
        headers = {
            'cookie': 'kg_mid=08c34c7abf0dcf79bdf13d81af607ed8; kg_dfid=08y7YV2ZFSgU1p9gmt0M9efs; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1649896123,1650548974,1650618280,1651034625; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1651035037',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
        }

        html = requests.get(url, headers=headers).text
        # print(html)
        # https://webfs.tx.kugou.com/202204271241/25aa465e3076a3c0fa9d4134c64cd821/KGTX/CLTX001/b52368ab77da9d5472408d8681b9e0c6.mp3
        # https://webfs.ali.kugou.com/202204271250/8b5c45677f118f3db93166f447950fad/KGTX/CLTX001/2076165fdcb580283fd394c178eeb411.mp3

        Hash_list = re.findall('"Hash":"(.*?)"', html)
        Album_id_list = re.findall('"album_id":(.*?),', html)
        # print(Hash_list)
        # print(Album_id_list)

        for Hash, album in zip(Hash_list, Album_id_list):
            # print(Hash, album)

            # 获取请求，对音乐数据包发起请求
            index_url = 'https://wwwapi.kugou.com/yy/index.php'
            params = {
            'r': 'play/getdata',
            # 'callback': 'jQuery19108388130387774893_1651034632058',
            'hash': Hash,
            'dfid': '08y7YV2ZFSgU1p9gmt0M9efs',
            'appid': '1014',
            'mid': '08c34c7abf0dcf79bdf13d81af607ed8',
            'platid': '4',
            'album_id': album,
            '_': '1651034632065',
                }
            html1 = requests.get(url=index_url, params=params, headers=headers)
            # print(html1.json())
            title = html1.json()['data']['audio_name']
            v_url = html1.json()['data']['play_url']
            print(title, v_url)
            pool.submit(v_url, title)

            try:
                v_content = requests.get(v_url).content
            except Exception as e:
                v_content = requests.get(url='https://webfs.ali.kugou.com/202204271421/a8f26ba57a68b2fcd8ed1c38a4f9162c/KGTX/CLTX001/a4ea497d274cf9e96560a41a864a14bc.mp3').content
            filename = 'kugou'
            if not os.path.exists(filename):
                os.makedirs(filename)
            with open('kugou/{}.mp3'.format(title), mode='ab')as f:
                f.write(v_content)
    end = time.time()
    print(f'执行时间:{end - start:.3f}秒')