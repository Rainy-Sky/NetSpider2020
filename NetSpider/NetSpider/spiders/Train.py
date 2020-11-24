# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TrainSpider(CrawlSpider):
    name = 'Train'
    allowed_domains = ['huoche.8684.cn/']

    local_time = time.strftime("%Y%m%d",time.localtime())
    base_url = "http://huoche.8684.cn/p_武汉_北京?date="
    url = base_url + local_time
    start_urls = [url]

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
