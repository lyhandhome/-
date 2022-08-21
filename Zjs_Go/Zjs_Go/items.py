# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZjsGoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    punish_code = scrapy.Field()
    code = scrapy.Field()
    punish_Person = scrapy.Field()
    person = scrapy.Field()
    person_f = scrapy.Field()
    law_d = scrapy.Field()
    law = scrapy.Field()
    punish_date = scrapy.Field()
    date = scrapy.Field()
    f_text = scrapy.Field()
    text = scrapy.Field()
