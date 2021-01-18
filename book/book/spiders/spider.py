import scrapy
from bs4 import BeautifulSoup
import requests
import json
from scrapy.http import FormRequest

class BookSpider(scrapy.Spider):
    name = "book"
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'


    def start_requests(self):
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        headers = {'User-Agent': user_agent}
        # start_url = 'http://www.g2b.go.kr:8101/ep/result/facilBidResultDtl.do'
        start_urls=["http://auto.naver.com/bike/mainList.nhn"]
        # start_url="http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?taskClCds=&bidNm=%B5%B5%BC%AD&searchDtType=1&fromBidDt=2016/04/15&toBidDt=2016/05/15&fromOpenBidDt=&toOpenBidDt=&radOrgan=1&instNm=&area=&regYn=Y&bidSearchType=1&searchType=1"

        custom_settings= {
            'DOWNLOADER_MIDDLEWARES': { 
                'crawler.middlewares.BookDownloaderMiddleware': 100 
            }
        }   

        # done="개찰완료".encode('euc-kr')

        # payload={'bidno': '20160514664', 'bidseq': '00', 'bidcate' : '0', 'rebidno': '0', 'progressInfo':done }
        # yield scrapy.Request(url = start_url, method="POST", body=json.dumps(payload),callback = self.parse)

        

    def parse(self, response):
    

        print("\n\n\n\n---------- THIS IS PARSE RESULT ----------\n")
        print(response)
        # print(response.xpath("//*").extract())
        


        

        print("\n----------------------------------------\n\n\n\n")

    def parseAnnouncement(self, ansRes):
        
        print("\n\n\n\n---------- THIS IS RESULT ----------\n")
        
        # print(type(ansRes))
        print(ansRes.url)
       

        print("\n----------------------------------------\n\n\n\n")
