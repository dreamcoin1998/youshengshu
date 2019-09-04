# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YoushengshuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book = scrapy.Field() # 有声书书名
    category = scrapy.Field() # 书的类别
    author = scrapy.Field() # 书作者
    broadcaster = scrapy.Field() # 播音
    pub_time = scrapy.Field() # 发布时间
    status = scrapy.Field() # 状态
    link = scrapy.Field() # 书的链接
