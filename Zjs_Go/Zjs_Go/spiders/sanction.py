import scrapy
from ..items import *
from redis import Redis

class SanctionSpider(scrapy.Spider):
    name = 'sanction'
    allowed_domains = ['www.zjzwfw.gov.cn']
    start_urls = ['https://www.zjzwfw.gov.cn/zjservice/matter/punishment/index.do']
    base_url = 'https://www.zjzwfw.gov.cn/zjservice/matter/punishment/searchallpunishlist.do'
    # https://www.zjzwfw.gov.cn/zjservice/matter/punishment/searchallpunishlist.do?pageNo=45
    # 创建redis链接对象
    conn = Redis(host='127.0.0.1', port=6379, password='handhome')
    def parse(self, response):
        # 遍历每一页的数据获取url 总共284588页
        for i in range(1, 50001):  # 284588 # 5001 -->10001 -->15001 -->20001
            url = '%s?pageNo=%s' % (self.base_url, i)
            yield scrapy.Request(url, callback=self.parse_html)

    def parse_html(self, response):
        for s in response.xpath('//table[@class="xzcf_lb"]/tr'):
            # href = response.urljoin(href)

            href = s.xpath('./td/a/@href').extract_first()
            if href:
                href = response.urljoin(href)
                # 将详细页的url存入redis的set中
            ex = self.conn.sadd('urls', href)
            if ex == 1:
                # print('该url没有被爬取过, 可以进行数据爬取')
                yield scrapy.Request(href, callback=self.parse_item)

    def parse_item(self, response):

        title = response.xpath('//table/tr/td[@align="center"]/text()').extract_first()
        punish_code = response.xpath('//table[@class="xzcf_bg"]/tr/td[2]/text()').extract_first()
        code = response.xpath('//table[@class="xzcf_bg"]/tr/td[3]/text()').extract_first()
        punish_Person = response.xpath('//table[@class="xzcf_bg"]/tr[2]/td[2]/text()').extract_first()
        persion = response.xpath('//table[@class="xzcf_bg"]/tr[2]/td[@class="xzcf_xx"]/text()').extract()[0]
        person = ''.join(persion).split()[0]
        try:
            person_f = response.xpath('//table[@class="xzcf_bg"]/tr[2]/td[@class="xzcf_xx"]/text()').extract()[1]
        except:
            person_f = ''
        law_d = response.xpath('//table[@class="xzcf_bg"]/tr[3]/td[2]/text()').extract_first()
        law = response.xpath('//table[@class="xzcf_bg"]/tr[3]/td[3]/text()').extract_first()
        punish_date = response.xpath('//table[@class="xzcf_bg"]/tr[4]/td[2]/text()').extract_first()
        date = response.xpath('//table[@class="xzcf_bg"]/tr[4]/td[3]/text()').extract_first()
        f_text = response.xpath('//table/tr/td[@width="270"]/text()').extract_first()
        text = response.xpath('//table/tr/td[@class="xzcf_jds"]/p/text()').extract()
        text = ''.join(text).split()

        item = ZjsGoItem()
        item['title'] = title
        item['punish_code'] = punish_code
        item['code'] = code
        item['punish_Person'] = punish_Person
        item['person'] = person
        item['person_f'] = person_f
        item['law_d'] = law_d
        item['law'] = law
        item['punish_date'] = punish_date
        item['date'] = date
        item['f_text'] = f_text
        item['text'] = text

        # print(item)
        yield item
