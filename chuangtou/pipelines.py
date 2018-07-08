# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class ChuangtouPipeline(object):

    def open_spider(self, spider):
        self.fp = open('ke.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        jsonstr = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.fp.write(jsonstr)
        return item

    def close_spider(self, spider):
        self.fp.close()