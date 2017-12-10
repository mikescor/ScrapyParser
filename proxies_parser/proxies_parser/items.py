# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProxiesParserItem(scrapy.Item):
    ip_address = scrapy.Field()
    port = scrapy.Field()
