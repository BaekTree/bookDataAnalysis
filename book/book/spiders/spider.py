import scrapy
from bs4 import BeautifulSoup
import requests
class BookSpider(scrapy.Spider):
    name = "book"
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'


    def start_requests(self):
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        headers = {'User-Agent': user_agent}
        start_url = 'http://www.g2b.go.kr/pt/menu/selectSubFrame.do?framesrc=/pt/menu/frameTgong.do?url=http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?taskClCds=&bidNm=%B5%B5%BC%AD&searchDtType=1&fromBidDt=2020/12/17&toBidDt=2021/01/16&fromOpenBidDt=&toOpenBidDt=&radOrgan=1&instNm=&area=&regYn=Y&bidSearchType=1&searchType=1'

        yield scrapy.Request(url = start_url, callback = self.parse, meta={'start_url':start_url})

    def parse(self, response):
    

        print("\n\n\n\n---------- THIS IS PARSE RESULT ----------\n")
        print(response)
        # 공고 announcement 파악
        # ans=response.xpath("//*[@id='resultForm']/div[2]/table/tbody/tr[2]/td[4]/div/a[1]/@href").extract()
        # print(ans)
        # print(response.xpath("//*[@id='resultForm']/div[2]/table/tbody/tr[2]/td[4]/div/a[1]/@href").extract())

        # 마감 여부 # 투찰 마감이 되어야 실제 어떻게 사람들이 입찰했는지 정보 파악 가능. 마감 표시가 없으면 정보 자체가 없다!
        # isEnd=response.xpath("//*[@id='resultForm']/div[2]/table/tbody/tr[2]/td[10]/div/text()").extract()
        # print(isEnd)


        # for 문 만들 때 이거 사용하기!
        # if endStr != None:
        # endStr=isEnd[0]
        # print(endStr)

        # if endStr == "마감":
            # print(True)

            
            # ansUrl=ans[0]
            # print(ansUrl)
            # yield scrapy.Request(url = ansUrl, callback = self.parseAnnouncement)
        


        

        print("\n----------------------------------------\n\n\n\n")

    def parseAnnouncement(self, ansRes):
        
        print("\n\n\n\n---------- THIS IS RESULT ----------\n")
        
        # print(type(ansRes))
        print(ansRes.url)
        # ansResStr=""+ansRes
        # print(ansResStr[5:])
        # ansRes.url

        # print(ansRes.xpath("//*[@id='container']/div[26]/table/tbody/tr/td[5]/a[1]").extract())
        """
            공고 디테일 페이지로 가려고 하면 href="javascript:toDetail(\'3\',%20\'20150123585\',%20\'00\',%20\'0\',%20\'0\',%20\'%EA%B0%9C%EC%B0%B0%EC%99%84%EB%A3%8C\');
            이 값을 보여준다. 즉 자바스크립트 함수를 실항하고 해당 url을 만들기 위한 인자를 보낸다.
            해당 자바스크립트 함수 toDetail를 확인하기 위해서 다시 scrapy 함수를 실행해보자

        """


        # res=response.xpath("//*[@id='resultForm']/div[2]/table/tbody/tr[1]/td[4]/div/a[1]/@href").extract()
        # url=res[0]
        # yield scrapy.Request(url = url, callback = self.parse)
        # print(url)

        print("\n----------------------------------------\n\n\n\n")
