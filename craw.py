from bs4 import BeautifulSoup
import requests
# class BookSpider(scrapy.Spider):
#     name = "book"
#     user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'


#     def start_requests(self):
#         user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
#         headers = {'User-Agent': user_agent}
start_url = 'http://www.g2b.go.kr/pt/menu/selectSubFrame.do?framesrc=/pt/menu/frameTgong.do?url=http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?taskClCds=&bidNm=%B5%B5%BC%AD&searchDtType=1&fromBidDt=2020/12/16&toBidDt=2021/01/15&fromOpenBidDt=&toOpenBidDt=&radOrgan=1&instNm=&area=&regYn=Y&bidSearchType=1&searchType=1'

#         yield scrapy.Request(url = start_url, callback = self.parse, meta={'start_url':start_url})

    # def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # result = response.url.split("/")[-2]
print("\n\n\n\n---------- THIS IS RESULT ----------\n")
        # print(response)  
        # print(response.xpath("//*[@id='container']/div[2]/table/tr[7]/td[11]/div/a"))
# start_url = response.meta['start_url']
response = requests.get(start_url)
# response.encoding = 'utf-8'
source = response.text
soup = BeautifulSoup(source, 'html.parser')
print(soup)
# # with open(filename, 'wb') as f:
# #     f.write(response.body)
print("\n----------------------------------------\n\n\n\n")
