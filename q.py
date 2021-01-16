# from urllib2 import Request, urlopen
from urllib.request import urlopen,Request
from urllib.parse import urlencode, quote_plus

# from urllib import urlencode, quote_plus

url = 'http://apis.data.go.kr/1230000/ScsbidInfoService/getOpengResultListInfoThngPreparPcDetail'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '서비스키', quote_plus('numOfRows') : '10', quote_plus('pageNo') : '1', quote_plus('inqryDiv') : '1', quote_plus('inqryBgnDt') : '201605010000', quote_plus('inqryEndDt') : '201605052359', quote_plus('bidNtceNo') : '20130715059', quote_plus('type') : 'json' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print (response_body)
