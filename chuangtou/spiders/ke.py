# -*- coding: utf-8 -*-
import scrapy
import json
from chuangtou.items import ChuangtouItem
from scrapy_redis.spiders import RedisSpider

class KeSpider(RedisSpider):
    name = 'ke'
    allowed_domains = ['rong.36kr.com']
    url = 'https://rong.36kr.com/n/api/org/51/investment?page='
    page = 1
    count = 1
    # start_urls = [url + str(page)]
    redis_key = 'Kespider:start_urls'


    def parse(self, response):
        html = json.loads(response.text)
        totalPages = html['data']['investments']['totalPages']
        print(totalPages)
        total = html['data']['investments']['data']
        for i in total:
            item = ChuangtouItem()
            item['phase'] = []
            item['fundsAmount'] = []
            for j in i['investments']:
                item['phase'].append(j['phase'])
                item['fundsAmount'].append(j['fundsAmount'])
            item['brief'] = i['project']['brief']
            item['logo'] = i['project']['logo']
            item['industry'] = i['project']['industry']
            item['companyName'] = i['project']['companyName']
            print('第%d保存完成' % self.count)
            self.count += 1
            yield item
        if self.page < totalPages:
            self.page += 1
            next_url = self.url + str(self.page)
            yield scrapy.Request(url=next_url, callback=self.parse)
