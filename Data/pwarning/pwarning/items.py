# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PwItem(scrapy.Item):
    # define the fields for your item here like:
    Date = scrapy.Field() 
    Symbol = scrapy.Field()
    Company = scrapy.Field()
    CurrR = scrapy.Field()
    NewR = scrapy.Field()
    Period = scrapy.Field()
    
