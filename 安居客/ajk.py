import xlwt
import requests
from bs4 import BeautifulSoup

from download import get_proxies

wb = xlwt.Workbook('utf-8')
sheet = wb.add_sheet('张掖')
col_names = ('排名', '联系', '名称', '房子样式', '面积', '朝面', '层', '小区', '地址', '年份', '价格', '平方')
for index, name in enumerate(col_names):
    sheet.write(0, index, name)

rank = 0
for i in range(1,51):
    url = f'https://zhangye.anjuke.com/sale/p{i}/?from=SearchBar'
# url = 'https://zhangye.anjuke.com/sale/?from=SearchBar'
    headers = {
        'Cookie': 'ctid=388; cmctid=10454; aQQ_ajkguid=05D42A6C-EFBF-F48F-2550-E5ED1D4D4308; id58=CpQCJWJqpTi5dd5QTLI2Ag==; _ga=GA1.2.2113859244.1651827607; _gid=GA1.2.842798142.1651827607; wmda_new_uuid=1; wmda_uuid=fdba81ed6071045d422f29fe7404a645; wmda_visited_projects=%3B6289197098934; 58tj_uuid=a53b8280-e739-4d8c-82ff-66b171f7fc33; als=0; ajk-appVersion=; fzq_h=9e47626e303e3cd5efa0a9d118db3218_1651827616659_7d59231f235b4d9198c5cab7aeed465b_710776628; isp=true; sessid=DE113BEB-976C-4F53-7553-B00A65538099; twe=2; new_uv=2; fzq_js_anjuke_ershoufang_pc=cbbc6537d5b434b1b25958a4005f0480_1651831303042_24; obtain_by=1; xxzl_cid=cbd88ffa42154956a590d3983a906d7c; xzuid=1a5d6138-c455-487a-b02f-51c17aa2f136',
        'Host': 'zhangye.anjuke.com',
        'Referer': 'https://zhangye.anjuke.com/sale/ganzhouqu/?from=SearchBar',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    }
    # 设置ip代理
    html = requests.get(url, headers=headers, proxies=get_proxies()).text
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    datas = soup.select('div.property')
    # print(datas)
    for d in datas:
        rank += 1
        # 获取房子地址
        title = d.select_one('a h3').text
        # print(title)

        # 获取房子的大小样式
        spec = d.select_one('.property-content-info p').text.replace(' ', '')
        # print(spec)

        # 获取房子面积
        area = d.select_one('.property-content-info >p:nth-child(2)').text.split()[0]
        # print(area)

        # 获取房子在哪面
        area1 = d.select_one('.property-content-info >p:nth-child(3)').text.split()[0]
        # print(area1)

        # 获取房子在哪一层
        try:
            height = d.select_one('.property-content-info >p:nth-child(4)').text.split()[0]
            # print(height)
        except Exception as e:
            height = '无'
            # print(height)

        # 获取房子哪一年建造
        try:
            date = d.select_one('.property-content-info >p:nth-child(5)').text.split()[0]
            print(date)
        except Exception as e:
            date = '今年建造'
            print(date)

        # 获取房子在哪个小区
        community = d.select_one('p.property-content-info-comm-name').text
        # print(community)

        # 获取房子具体地址
        address = d.select_one('p.property-content-info-comm-address').text
        # print(address)

        # 获取联系人
        try:
            contact = d.select_one('div.property-extra-wrap > div > span:nth-child(4)').text
            print(contact)
        except Exception as e:
            contact = '私人'
            print(contact)

        # 房子的价格
        price = d.select_one('p.property-price-total').text.replace(' ', '')
        print(price)

        # 每平米
        price1 = d.select_one('p.property-price-average').text
        print(price1)


        data_list = [rank, contact, title, spec, area, area1, height, community, address, date, price1,price]
        for index, item in enumerate(data_list):
            sheet.write(rank, index, item)

    wb.save('房价.xls')
    print('程序结束...')
