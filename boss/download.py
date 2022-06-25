import requests
def get_proxies():
    print('--------使用了代理-----------')
    p_url = 'http://api.tianqiip.com/getip?secret=kg2oayp463hviei8&type=json&num=1&time=3&port=1'
    data = requests.get(p_url).json()['data'][0]
    proxy = data['ip'] + ':' + str(data['port'])
    proxies = {
        'http://': proxy,
        'https://': proxy,
    }
    # print(proxies)
    return proxies
# get_proxies()
# for i in range(16, 19):
#     url = f'https://www.zhipin.com/c100010000-p100109/?query=%E7%88%AC%E8%99%AB%E5%AE%9E%E4%B9%A0%E7%94%9F&page={i}&ka=page-{i}'
#     print(url)