# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import os
import time

class NetspiderPipeline(object):
    count = 0
    def __init__(self):  # 初始化，打开文件
        local_time = time.strftime("%Y_%m_%d", time.localtime())
        file_path = './data/'+local_time+'.json'
        if os.path.exists(file_path):
            os.remove(file_path)
        self.file = codecs.open(file_path, 'a+', encoding="utf-8")
        # self.file.write("{[\n")
        # 这里用codecs库来打开文件，目的是编码不会出错

    def process_item(self, item, spider):  # 写入文件
        lines = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.file.write(lines)
        return item
    def spider_closed(self, spider):  # 关闭文件
        # self.file.write("\n}")
        self.file.close()
