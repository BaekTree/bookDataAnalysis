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
        start_url = 'http://www.g2b.go.kr:8101/ep/result/facilBidResultDtl.do'
        ans_rul="http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?taskClCds=&bidNm=%B5%B5%BC%AD&searchDtType=1&fromBidDt=2016/04/15&toBidDt=2016/05/15&fromOpenBidDt=&toOpenBidDt=&radOrgan=1&instNm=&area=&regYn=Y&bidSearchType=1&searchType=1"

        """
        curl -d "bidno=20160514664&bidseq=00&bidcate=0&rebidno=0&progressInfo=%B0%B3%C2%FB%BF%CF%B7%E1" \
        -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36" \
        -H "Origin: http://www.g2b.go.kr:8081" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        -H "Referer: http://www.g2b.go.kr:8081/" \
        -X POST http://www.g2b.go.kr:8101/ep/result/facilBidResultDtl.do | iconv -c -f euc-kr -t utf-8 > output.xml
        """

        done="개찰완료".encode('euc-kr')

        payload={'bidno': '20160514664', 'bidseq': '00', 'bidcate' : '0', 'rebidno': '0', 'progressInfo':done }
        yield scrapy.Request(url = start_url, method="POST", body=json.dumps(payload),callback = self.parse)

        

        # return [FormRequest(url="http://www.g2b.go.kr:8101/ep/result/facilBidResultDtl.do",
        #                 formdata={'bidno': '20160514664', 'bidseq': '00', 'bidcate' : '0', 'rebidno': '0', 'progressInfo':'%B0%B3%C2%FB%BF%CF%B7%E1'},
        #                 callback=self.parse)]

# https://docs.scrapy.org/en/latest/topics/request-response.html


    # def test(self, response):
        # res=requests.post()
# {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# {'Accept-Encoding': 'gzip, deflate',
# {'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6',
# {'Cache-Control': 'max-age=0',
# {'Connection': 'keep-alive',
# {'Content-Length': '85',
# {'Content-Type': 'application/x-www-form-urlencoded',
# {'Cookie': 'ipmsperf_uuid=-3429498447481713841; keywords=%uB3C4%uC11C; ccsession=202101171457180000303f303f07f3; _KONEPS_PAGE=%3C%21%23%25%3EtbidListUrl%3C%40%25%7E%3E%2Fep%2Ftbid%2FtbidList.do%3Farea%3D%26bidNm%3D%25B5%25B5%25BC%25AD%26bidSearchType%3D1%26fromBidDt%3D2016%252F04%252F15%26fromOpenBidDt%3D%26instNm%3D%26radOrgan%3D1%26regYn%3DY%26searchDtType%3D1%26searchType%3D1%26taskClCds%3D%26toBidDt%3D2016%252F05%252F15%26toOpenBidDt%3D; G2B_EP2_PRC=eG1heXhFUWRwd0ZpalFQV2w0UTJPcjNQcTZEWVFQKzV0OFUxWXF2bjRDVkVTbS9mcDNpNzhSdUNpV3VtMVBXbApINUtwMWU5b3cra3lzN0ozeXRZWjFac2dxdk03TmpVRUlHanBwT2tIZlRFNkNzYWJmb3JTbGdlNXdERkJMelpQCmJTNG90ZVpKQ1A1L0lMbGhVdlpMK3ltTkhDQUFEd0l6ekxTZGhRWHpsaFFqcE1jZmlhWFNQbUxYOGFFVjBvQzcKT2s1TGl2TkFlb08rVm9JL29XNEk5ZllVRzZZRG9jaHIwN3FzK2xIaW55ZFV3SzRiTCtYNVN3cmtsYjNaMlNQZwpYOCtLU0JwWXdFS0pkV1Z1dEtMTUdNNmNGS3hCcElzTEh1UEE4RjV5Rlp5dSsxUG5CVFQ0RjAzd2gycURscFVXCmgyMDE4cHZYbHRQU053aCt3dTNhL0E9PUAjJCVeJipKN3RET0FyVENEZUI1MDg4MGdUUVFXcjJFVllxSEtnNi9BVUZvbjY0RGdvTjY4dTlJWm9BdDZzU2VyM3RwWjk3; JSESSIONID=SnKbgGKQQvxNH4rW12LhytzgkGXsTfppk3wNc3fTWdr83CWDWHzL!-1631601383',
# {'Host': 'www.g2b.go.kr:8101',
# {'Origin': 'http://www.g2b.go.kr:8081',
# {'Referer': 'http://www.g2b.go.kr:8081/',
# {'Upgrade-Insecure-Requests': '1',
# {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'

        # return scrapy.FormRequest.from_response(
        #             response,
        #             formname='ebid',
        #             formid='ebid',
        #             formdata={'bidno': '20160514664', 'bidseq': '00', 'bidcate' : '0', 'rebidno': '0', 'progressInfo':'개찰완료','bidno2': '20160514664', 'bidseq2': '00', 'bidcate2' : '0', 'rebidno2': '0', 'progressInfo2':'개찰완료'},
        #             callback=self.parse
        #         )
                
    def parse(self, response):
    

        print("\n\n\n\n---------- THIS IS PARSE RESULT ----------\n")
        # print(response.url)
        # print(response.status)
        # print(response.headers)
        # print(response.body)
        # print(response.flags)

        # print(response.request)
        # print(response.url)
        # print(response.url)
        print(response.xpath("//*").extract())
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
