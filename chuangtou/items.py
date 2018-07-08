# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChuangtouItem(scrapy.Item):
    phase = scrapy.Field()
    fundsAmount = scrapy.Field()
    brief = scrapy.Field()
    logo = scrapy.Field()
    industry = scrapy.Field()
    companyName = scrapy.Field()
