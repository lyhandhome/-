import requests
from bs4 import BeautifulSoup
import pymysql


for i in range(1, 21):
    url = f'https://nj.lianjia.com/zufang/pg{i}/#contentList'
    # print(url)
    headers = {
        'Cookie': 'lianjia_uuid=2a6fccfb-fb27-4bed-8073-ccda9eee46b5; _smt_uid=619b4f66.365e47bf; UM_distinctid=17d46ae2a3446-052ef576fd8608-978183a-144000-17d46ae2a35832; _ga=GA1.2.1563705003.1637568361; Qs_lvt_200116=1637568364; Qs_pv_200116=4440498528430611500%2C2252446606793860900%2C2906888876667785000%2C3852336082168546000%2C2381896744941362000; _jzqx=1.1637575486.1637593794.2.jzqsr=nj%2Elianjia%2Ecom|jzqct=/ershoufang/.jzqsr=sz%2Efang%2Elianjia%2Ecom|jzqct=/; CNZZDATA1253492138=1933462495-1637558484-https%253A%252F%252Fwww.baidu.com%252F%7C1639978754; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217d46ae2b9e577-063e250b4d4bc1-978183a-1327104-17d46ae2b9f84%22%2C%22%24device_id%22%3A%2217d46ae2b9e577-063e250b4d4bc1-978183a-1327104-17d46ae2b9f84%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; CNZZDATA1256793290=1355252361-1637563185-https%253A%252F%252Fwww.baidu.com%252F%7C1639988312; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1647608377; lianjia_ssid=23f4a0c6-18c9-4c25-8642-8a52dcba4811; _jzqc=1; _jzqa=1.1626910246345120800.1637568359.1647608348.1651193015.8; _jzqy=1.1637568359.1651193015.1.jzqsr=baidu.-; _jzqckmp=1; _gid=GA1.2.953276916.1651193020; select_city=320100; _qzja=1.604763699.1637568359300.1639989128370.1651193039544.1639989128370.1651193039544.0.0.0.22.5; _qzjc=1; _qzjto=1.1.0; _jzqb=1.3.10.1651193015.1; CNZZDATA1254525948=182633902-1637566349-https%253A%252F%252Fwww.baidu.com%252F%7C1651186149; CNZZDATA1255633284=49519669-1637563814-https%253A%252F%252Fwww.baidu.com%252F%7C1651185068; CNZZDATA1255604082=1336298870-1637566569-https%253A%252F%252Fwww.baidu.com%252F%7C1651186755; _qzjb=1.1651193039544.1.0.0.0; GUARANTEE_BANNER_SHOW=true; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiZTAyN2FmYjdlN2EzNGM0MWRmYWRjMDYwNmYyOGFmODEwNDEzOTAyMWQ3OTk2ODg2ZDhjMzAyYWY1MTI0NDUyNGQ1YTM5MjUxNThhZGFjY2U5YjQwNWFmZmYwM2ZjOGViZDlhYTAxMTRjNzdkZDRjYTk1N2ZmYTAwYzVmMmQ2ZWMxZmQxYmU3ZmIwNTI5NzUwNTQxYjljNTY3MTIzMDU1ZTNjNjU0MGZlYzE5YmZlYzMyOWRmZGM4NGVhZDgwOWVkNmI3NDMyYTk3MTExZTNlNjcxMmI1ZTA3YzI2ZDNmMDQ2YmQ3NTQzYTA3N2QyYmFkMjcwMDU2YjVlZWUwZmY4MlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI3ZWMwNDczMVwifSIsInIiOiJodHRwczovL25qLmxpYW5qaWEuY29tL3p1ZmFuZy9wZzIvI2NvbnRlbnRMaXN0Iiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0=',
        'Host': 'nj.lianjia.com',
        'Referer': 'https://nj.lianjia.com/zufang/pg2/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    }
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    # print(soup)
    data_list = soup.select('.content__list--item')
    # print(data_list)
    data_all = []
    for d in data_list:
        title = d.select_one('a.twoline').text.split()[0]
        data_all.append(title)
        address = d.select_one('p.content__list--item--des').text.replace('\n', '').replace('/', '').split()
        data_all.append(address)
        address = ''.join(address).replace(',', '|')

        style = d.select_one('p.content__list--item--bottom').text.split()
        data_all.append(style)
        style = ''.join(style).replace(',', '')

        price = d.select_one('span.content__list--item-price').text.split()
        data_all.append(price)
        price = ''.join(price).replace(',', '')
        conn = pymysql.connect(
            host="127.0.0.1",
            user="root",
            passwd="1018",
            db="dd",
            port=3306,
            charset='utf8',
            autocommit=True

        )
        sql = "insert into rents(title,address,style,price)values('" + title + "','" + address + "','" + style + "','" + price + "')"
        print(sql)
        conn.query(sql)
        conn.close()
