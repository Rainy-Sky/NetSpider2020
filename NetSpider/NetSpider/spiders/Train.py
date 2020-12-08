# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from NetSpider.items import NetspiderItem

class TrainSpider(scrapy.Spider):
    name = 'Train'
    allowed_domains = ['huoche.8684.cn/']

    local_time = time.strftime("%Y%m%d", time.localtime())
    base_url = "https://huoche.8684.cn"
    link_url = "/p_武汉_北京?date="
    url = base_url + link_url + local_time
    start_urls = [url]

    # rules = (
    #     Rule(LinkExtractor(allow=r'huoche.8684.cn/p_武汉_北京?date='+local_time), callback='parse_url', follow=True),
    #     Rule(LinkExtractor(allow=r'/h_G\d'), callback='parse_item', follow=False),
    # )

    def parse(self, response):
        div_list = response.xpath('/html/body/div[@class="depth"]//div[@class="table-wrap"]/ol/li')
        print("step1")
        for div in div_list:
            url = div.xpath('./ul/li/a/@href')[0].extract()
            sec_url = self.base_url + url
            price = div.xpath('./ul/li[5]//i/text()')[0].extract()
            yield scrapy.Request(url=sec_url, callback=self.parse_item, dont_filter=True, meta={'price':price})

    def parse_item(self, response):
        print("step2")
        item = NetspiderItem()
        # div_list = response.xpath('/html/body/div[6]/div[3]/div[1]/div[1]/div')
        p_list = response.xpath('/html/body//div[@class="depth"]/div[3]/div[1]/div[1]/div[1]/p')
        div_list = response.xpath('/html/body//div[@class="depth"]/div[3]/div[1]/div[1]/div[1]/div')
        train = p_list[0].xpath('./span/text()')[0].extract()
        time_start = div_list[0].xpath('./div[1]/p[1]/text()')[0].extract()
        time_end = div_list[0].xpath('./div[3]/p[1]/text()')[0].extract()
        time_last = div_list[0].xpath('./div[2]/text()')[0].extract()
        info = p_list[1].xpath('./text()')[0].extract()

        item['train'] = train
        item['time_start'] = time_start
        item['time_end'] = time_end
        item['time_last'] = time_last
        item['price'] = response.meta['price']
        item['info'] = info

        stations = []
        tr_list = response.xpath('/html/body//div[@class="depth"]/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr')
        for tr in tr_list:
            station_name =  tr.xpath('./td[2]/a/text()')[0].extract()
            arrive_time = tr.xpath('./td[4]/text()')[0].extract()
            leave_time = tr.xpath('./td[5]/text()')[0].extract()
            wait_time = tr.xpath('./td[6]/text()')[0].extract()
            miles = tr.xpath('./td[7]/text()')[0].extract()

            station = {}
            station['station_name'] = station_name
            station['arrive_time'] = arrive_time
            station['leave_time'] = leave_time
            station['wait_time'] = wait_time
            station['miles'] = miles
            stations.append(station)
        item['stations'] = stations

        # print(train, time_start, time_end, time_last, info)
        yield item
