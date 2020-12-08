# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class NetspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    train = scrapy.Field()
    time_start = scrapy.Field()
    time_end = scrapy.Field()
    time_last = scrapy.Field()
    price = scrapy.Field()
    info = scrapy.Field()
    stations = scrapy.Field()

