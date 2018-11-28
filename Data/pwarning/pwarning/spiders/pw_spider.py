from scrapy import Spider
from scrapy.selector import Selector
from pwarning.items import PwItem
import scrapy # you need this to call scrapy.Request
from datetime import datetime


class pwSpider(Spider):
    name = "pw_spider"
    allowed_urls = ['http://www.rttnews.com']
    
    start = 1
    end = 8 # we now the page has 8 by default
    period = range(start,end+1,1)

    base = "http://www.rttnews.com/Calendar/ProfitWarnings.aspx?PageNum="

    start_urls = [base+str(i) for i in period] # scrapy iterates automatically once the first page is scrapped
  
    def parse(self, response):
        rows = response.xpath('//*[@id="mainlayout"]/div[2]/div[3]/div[2]/div').extract() # inspect html and you will see our elements are all <div>

        for row in rows[1:]: # rows[0] are only the columns names 
            Dat = Selector(text=row).xpath('//div[1]/text()').extract()[1].encode('utf-8','ignore')
            Dat = Dat.strip()[3:5] + '-' + Dat.strip()[0:2] + '-' + Dat.strip()[6:8]
            Date = datetime.strptime(Dat , '%d-%m-%y').date()

            # the next line below doesn't work because this xpath address contains ctl01 that changes for every row:
            # Symbol = Selector(text=row).xpath('//*[@id="ctl00_CPI_rptAnnouncement_ctl01_dvSymItem"]/a/text()').extract()[0].encode('utf-8','ignore')
            # solution: use xpath "contains" to leave out reference numbers:
            Symbol = Selector(text=row).xpath('//*[contains(@id,"dvSymItem")]/a/text()').extract()[0].encode('utf-8','ignore')
            # compnay has the same syntax problem so we use "contains" again:    
            Company = Selector(text=row).xpath('//*[contains(@id,"dvCompItem")]/a/text()').extract()[0].encode('utf-8','ignore').strip()
            CurrR = Selector(text=row).xpath('//div[4]/text()').extract()[0].encode('utf-8','ignore')
            NewR = Selector(text=row).xpath('//div[5]/text()').extract()[0].encode('utf-8','ignore')
            Period = Selector(text=row).xpath('//div[6]/text()').extract()[0].encode('utf-8','ignore')

            item = PwItem()
            
            item['Date'] = Date
            item['Symbol'] = Symbol
            item['Company'] = Company
            item['CurrR'] = CurrR
            item['NewR'] = NewR
            item['Period'] = Period
               
            yield item



    
