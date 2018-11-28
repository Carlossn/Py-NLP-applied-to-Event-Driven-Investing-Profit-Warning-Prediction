# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TransItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
 	Name = scrapy.Field()
 	Symbol = scrapy.Field()
 	Period = scrapy.Field()
 	Date = scrapy.Field()
 	Month = scrapy.Field()
 	Year = scrapy.Field()
 	Target = scrapy.Field()
 	Text = scrapy.Field()