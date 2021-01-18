import scrapy
from bs4 import BeautifulSoup
import requests
import json
from scrapy.http import FormRequest

import pandas as pd

class BookSpider(scrapy.Spider):
    name = "book"
    # user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    # start_rul="http://auto.naver.com/bike/mainList.nhn"
    start_urls = ["http://www.g2b.go.kr:8081/ep/invitation/publish/bidInfoDtl.do?bidno=20160514754&bidseq=00&releaseYn=Y&taskClCd=1"]

    custom_settings= {
        'DOWNLOADER_MIDDLEWARES': { 
            'book.middlewares.BookDownloaderMiddleware': 100 
        }
    }

    def parse(self, response):
        print("\n\n\n\n---------- THIS IS PARSE RESULT ----------\n")
        # print(response.text)
        # print(response.xpath("//*").extract())

        # url = response.url
        
        tb=pd.read_html(response.text)

        # type of tb : list
        # print(type(tb))
        
        # 2nd table is our target
        # for (i,t) in enumerate(tb):
        #     print("" + str(i) + "th table : ")
        #     print(t)

        print(tb[1])

        



        

        print("\n----------------------------------------\n\n\n\n")

    def parseAnnouncement(self, ansRes):
        
        print("\n\n\n\n---------- THIS IS RESULT ----------\n")
        
        # print(type(ansRes))
        print(ansRes.url)
       

        print("\n----------------------------------------\n\n\n\n")
