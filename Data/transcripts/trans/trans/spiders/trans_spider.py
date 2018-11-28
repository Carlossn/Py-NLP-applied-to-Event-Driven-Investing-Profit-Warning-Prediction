from scrapy import Spider
from scrapy.selector import Selector
from trans.items import TransItem
import scrapy # you need this to call scrapy.Request
from datetime import datetime
from fake_useragent import UserAgent # random user_agent to dodge website ban
import re
import pandas as pd

class transSpider(Spider):
    name = "trans_spider"
    allowed_urls = ['http://seekingalpha.com']
    
    # 2 choices:
    # 1) Scraping event stocks: ticker_load.csv and target=1
    # 2) Scraping non-event stocks: ticker_load_no_pw.csv

    ticker_l = list(pd.read_csv('ticker_load_no_pw.csv', header = None)[0])[12:15] # select ticker_load.csv and target=1 
    user_rd = UserAgent().random
    per = 5 # number of conference calls to retrieve
    target = 0 # 1 when the ticker_l has companies that are impacted by the event and 0 otherwise.

    def start_requests(self):
        urls = ['http://seekingalpha.com/symbol/'+i+'/earnings/transcripts' for i in self.ticker_l]
        
        for url in urls:
            yield scrapy.Request(url, callback=self.parse, headers={'User-Agent':self.user_rd})  #headers={'User-Agent':self.user_rd}

           

    def parse(self, response):
        rows = response.xpath('//*[@id="headlines_transcripts"]/div/ul/li/div/div/a[contains(@href,"transcript")]').extract() # only conf call transcripts considered
        link_l = []

        for row in rows[1:(self.per+1)]: # rows[0] are only the columns names 
            l = Selector(text=row).xpath('//@href').extract() # use empty list [] as condition to reject right below:
            if l!=[]:
                link_l.append('http://seekingalpha.com' + l[0].encode('utf-8', 'ignore')) # this creates the list of movies links for a specific year/top studio. The conditional eliminates empty objects

        for link in link_l: # for every link (earnings call transcript) in our list, opens a door to scrap it:
            yield scrapy.Request(link, callback=self.trans_details,headers={'User-Agent':self.user_rd}) # creates a new request for link that creates a new response object.

    def trans_details(self, response): # called  by the line above and works around a new response object

        tab = response.xpath('//*[@id="a-body"]/p').extract()
        
        Name = Selector(text=tab[0]).xpath('//text()').extract()[0].encode('utf-8', 'ignore')
        Name = Name[0:len(Name)-6]
        
        # Ticker = Selector(text=tab[0]).xpath('//p[1]/a/text()').extract()[0].encode('utf-8', 'ignore')  
        Ticker = Selector(text=tab[0]).xpath('//text()').extract()[0].encode('utf-8', 'ignore')  


        Period = Selector(text=tab[1]).xpath('//text()').extract()[0].encode('utf-8', 'ignore')[0:7].replace(" ","")
        
        Date = Selector(text=tab[2]).xpath('//text()').extract()[0].encode('utf-8', 'ignore')
        Date = Date[0:len(Date)-8].strip()
        Date = re.sub('[\n,.-]', ' ', Date)
        year = re.search('20..', Date).group()
        day = re.search('[1-31].', Date).group()
        month = re.search('[A-z]+', Date[0:10]).group()
        month_dt ={
            'January': '01', 'February':'02', 'March':'03', 'April':'04','May':'05', 'June':'06',
            'July':'07', 'August':'08', 'September':'09', 'October':'10', 'November':'11', 'December':'12'   
        }
        month = month_dt[month]
        date = str(year)+'-'+str(month)+'-'+str(day)
        Date = datetime.strptime(date, '%Y-%m-%d').date()

        Text=[]
        for t in tab[0:(len(tab)-4)]:
            Line = Selector(text=t).xpath('//text()').extract()[0].encode('utf-8', 'ignore')
            Text.append(Line)

        item = TransItem()
            
        item['Name'] = Name
        item['Symbol'] = Ticker
        item['Period'] = Period
        item['Date'] = Date
        item['Month'] = month
        item['Year'] = year
        item['Target'] = transSpider.target
        item['Text'] = Text #str(' '.join(Text))
               
        yield item

