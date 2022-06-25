import requests
import pymysql

def get_proxies():
    print('--------使用了代理-----------')
    p_url = 'http://api.tianqiip.com/getip?secret=kg2oayp463hviei8&type=json&num=1&time=3&port=1'
    data = requests.get(p_url).json()['data'][0]
    proxy = data['ip'] + ':' + str(data['port'])
    proxies = {
        'http://': proxy,
        'https://': proxy,
    }
    return proxies

def save_mysql():
    conn = pymysql.connect(
        host="127.0.0.1",
        user="root",
        passwd="1018",
        db="数据库",
        port="3306",
        charset='utf-8',
        autocommit=True

    )
    sql = "insert into '表'()values ()"
    print(sql)
    conn.query(sql)
    conn.close()


# for i in range(1,51):
#     url = f'https://zhangye.anjuke.com/sale/p{i}/?from=SearchBar'
#     print(url)