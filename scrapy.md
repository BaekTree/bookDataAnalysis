# 스크래피 문서
스파이더를 통해서 크롤링을 해보면 
맨 처음 주소만 잡아주고
나머지는 안잡아준다!

설정에서 robot policy false으로 설정해도 같은 결과

검색 검색...

dynamic loading pages는 안된다고 함.



스크래피로만 시도. soup을 사용하지 않고 해보겠다.



scrapy fetch --nolog 'http://www.g2b.go.kr/pt/menu/selectSubFrame.do?framesrc=/pt/menu/frameTgong.do?url=http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?taskClCds=&bidNm=%B5%B5%BC%AD&searchDtType=1&fromBidDt=2020/12/16&toBidDt=2021/01/15&fromOpenBidDt=&toOpenBidDt=&radOrgan=1&instNm=&area=&regYn=Y&bidSearchType=1&searchType=1' > response.html


---

경기 도서 서적 최근 3개월
http://www.g2b.go.kr/pt/menu/selectSubFrame.do?framesrc=/pt/menu/frameTgong.do?url=http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?taskClCds=&bidNm=%B5%B5%BC%AD&searchDtType=1&fromBidDt=2020/12/16&toBidDt=2021/01/15&fromOpenBidDt=&toOpenBidDt=&radOrgan=1&instNm=&area=&regYn=Y&bidSearchType=1&searchType=1

여기에서 다시 fetch을 해보자
scrapy fetch --nolog 'http://www.g2b.go.kr/pt/menu/selectSubFrame.do?framesrc=/pt/menu/frameTgong.do?url=http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?taskClCds=&bidNm=%B5%B5%BC%AD&searchDtType=1&fromBidDt=2020/12/16&toBidDt=2021/01/15&fromOpenBidDt=&toOpenBidDt=&radOrgan=1&instNm=&area=&regYn=Y&bidSearchType=1&searchType=1'

나온 값
http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?taskClCds=&bidNm=%B5%B5%BC%AD&searchDtType=1&fromBidDt=2020/12/16&toBidDt=2021/01/15&fromOpenBidDt=&toOpenBidDt=&radOrgan=1&instNm=&area=&regYn=Y&bidSearchType=1&searchType=1


공고현황
http://www.g2b.go.kr/pt/menu/selectSubFrame.do?framesrc=/pt/menu/frameTgong.do?url=http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?taskClCds=&bidNm=%B5%B5%BC%AD&searchDtType=1&fromBidDt=2020/12/16&toBidDt=2021/01/15&fromOpenBidDt=&toOpenBidDt=&radOrgan=1&instNm=&area=&regYn=Y&bidSearchType=1&searchType=1

개찰결과
http://www.g2b.go.kr/pt/menu/selectSubFrame.do?framesrc=/pt/menu/frameTgong.do?url=http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?taskClCds=&bidNm=%B5%B5%BC%AD&searchDtType=1&fromBidDt=2020/12/16&toBidDt=2021/01/15&fromOpenBidDt=&toOpenBidDt=&radOrgan=1&instNm=&area=&regYn=Y&bidSearchType=1&searchType=1

전부 다 최신 공고로 간다.
검색 해보니...
http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?taskClCds=&bidNm=%BA%B8%BE%C8&searchDtType=1&fromBidDt=2016/04/15&toBidDt=2016/05/15&fromOpenBidDt=&toOpenBidDt=&radOrgan=1&instNm=&area=&regYn=Y&bidSearchType=1&searchType=1
이 주소는 2016년의 과거 주소로 가진다.

아까 안되는 주소와 비교해보자.
http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?taskClCds=&bidNm=%B5%B5%BC%AD&searchDtType=1&fromBidDt=2020/12/16&toBidDt=2021/01/15&fromOpenBidDt=&toOpenBidDt=&radOrgan=1&instNm=&area=&regYn=Y&bidSearchType=1&searchType=1

차이가 bidNm만 다르다. 그리고 날짜...

그럼 나온 bidNm에 날짜만 나도 과거로 해보자...
http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?taskClCds=&bidNm=%B5%B5%BC%AD&searchDtType=1&fromBidDt=2016/04/15&toBidDt=2016/05/15&fromOpenBidDt=&toOpenBidDt=&radOrgan=1&instNm=&area=7&regYn=Y&bidSearchType=1&searchType=1
된다!

지금은 안되는데? 다시 만들어서 비교해보자

http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?taskClCds=&bidNm=%B5%B5%BC%AD&searchDtType=1&fromBidDt=2016/04/15&toBidDt=2016/05/15&fromOpenBidDt=&toOpenBidDt=&radOrgan=1&instNm=&area=&regYn=Y&bidSearchType=1&searchType=1
이건 다시 된다. 뭐가 다르지?
둘째 줄에 area=7이 붙어서 안된다.

그래서 저 페이지에서 각 공고를 누르면 다음 url으로 들어간다.
http://www.g2b.go.kr:8081/ep/invitation/publish/bidInfoDtl.do?bidno=20160514754&bidseq=00&releaseYn=Y&taskClCd=1
포트가 8081으로 바뀌었다. 그리고 여기는 bidno와 bidseq, taskClCd만 다르게 하면 원하는 상세 공고로 들어갈 수 있다.

그리고 여기에서 개찰완료 버튼을 누르면 다음 url으로 진입
http://www.g2b.go.kr:8101/ep/result/facilBidResultDtl.do
상세 주소가 숨겨져 있다. 그리고 포트도 8101으로 다시 바뀐다.


데이터를 보낼 때
http://www.g2b.go.kr:8101/ep/result/facilBidResultDtl.do으로 post으로 보낸다.
개찰완료 버튼을 누르면 자바스크립트 함수 toDetail을 실행한다.
```
<a class="btn_mdl" href="javascript:toDetail('3', '20160514664', '00', '0', '0', '개찰완료');"><span>개찰완료</span></a>
```



공고 상세 페이지의 함수들은 이렇게 생겼다.
공고 상세 페이지 : http://www.g2b.go.kr/pt/menu/selectSubFrame.do?framesrc=/pt/menu/frameTgong.do?url=http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?taskClCds=&bidNm=%B5%B5%BC%AD&searchDtType=1&fromBidDt=2020/12/17&toBidDt=2021/01/16&fromOpenBidDt=&toOpenBidDt=&radOrgan=1&instNm=&area=&regYn=Y&bidSearchType=1&searchType=1

여기에서 자바스크립트 toDetail함수는 이렇게 생겼다.
```
	// 개찰결과 상세
	function toDetail(taskClCd, bidno, bidseq, bidcate, rebidno, progressInfo){
		var dtlUrl = "";
		
		if(taskClCd == "1" || taskClCd == "9"){	// 물품, 조달청 일반용역 
			dtlUrl = nquryhost + "/ep/result/prodBidResultDtl.do";
		}
		if(taskClCd == "2"){	// 외자 
			dtlUrl = nquryhost + "/ep/result/selectFrnBidResultDtl.do";
		}
		if(taskClCd == "3"){	// 공사
			dtlUrl = nquryhost + "/ep/result/facilBidResultDtl.do";
		}
		if(taskClCd == "4"){	// 비축
			dtlUrl = nquryhost + "/ep/result/stplBidResultDtl.do";
		}
		if(taskClCd == "5"){	// 용역
			dtlUrl = nquryhost + "/ep/result/serviceBidResultDtl.do";
		}
		if(taskClCd == "6" || taskClCd == "7"){	// 리스
			dtlUrl = nquryhost + "/ep/result/leaseBidResultDtl.do";
		}
		
		document.ebid.bidno.value = bidno;
		document.ebid.bidseq.value = bidseq;
		document.ebid.bidcate.value = bidcate;
		document.ebid.rebidno.value = rebidno;
		document.ebid.progressInfo.value = progressInfo;
		document.ebid.method = "post";
		document.ebid.action = dtlUrl;
		document.ebid.submit();
		return;
	}
```

여기에 document.ebid property가 있다.
```
<form method="post" id="ebid" name="ebid" action="">
				<input type="hidden" id="bidno2" name="bidno" value="">
				<input type="hidden" id="bidseq2" name="bidseq" value="">
				<input type="hidden" id="bidcate2" name="bidcate" value="">
				<input type="hidden" id="rebidno2" name="rebidno" value="">
				<input type="hidden" id="progressInfo2" name="progressInfo">
</form>
```


정리해보면, 사용자가 개찰완료 버튼을 누르면 현재 페이지에서 데이터를 form id 의 property으로 넣는다.
그리고 post함수를 실행해서 정보를 가지고 온다.
보내는 URL은 일반 물품이라면 nquryhost + "/ep/result/prodBidResultDtl.do";일 것이다.

nquryhost가 뭔지는 파악이 어려웠지만, 실제 도착한 페이지의 주소는 위에 적은 것처럼 http://www.g2b.go.kr:8101/ep/result/facilBidResultDtl.do
으로 보낸다.

결국 포트번호 8101으로 물품에 맞춰서 facil으로 보내되, form의 input 값들만 넣어서 보내보면 되지 않을까?!

시도해보자! 

scrapy의 post request
```
return [FormRequest(url="http://www.example.com/post/action",
                    formdata={'name': 'John Doe', 'age': '27'},
                    callback=self.after_post)]
```

여기에 현재 문제에 해당하는 값들을 넣어보자.
```
        document.ebid.bidno.value = bidno;
		document.ebid.bidseq.value = bidseq;
		document.ebid.bidcate.value = bidcate;
		document.ebid.rebidno.value = rebidno;
		document.ebid.progressInfo.value = progressInfo;
        <a class="btn_mdl" href="javascript:toDetail('3', '20160514664', '00', '0', '0', '개찰완료');"><span>개찰완료</span></a>



```

```
return [FormRequest(url="http://www.g2b.go.kr:8101/ep/result/facilBidResultDtl.do",
                    formdata={'bidno': '20160514664', 'bidseq': '00', 'bidcate' : '0', 'rebidno': '0', 'progressInfo':'개찰완료'},
                    callback=self.after_post)]
```
---


1. 해당 페이지에서 반복문으로 각 공고 들어가야 한다. for 사용해서 들어가고, tr[i]으로 조절할 수 있는 것 같다.
여기서 t[10]이 마감이면 그냥 continue으로 다음 index 공고로 보내버리고. 아닌 경우에 진행.
진행 할 때도 마감이 떠 있어야 해당 url으로 접속해서 다음 단계로 진행

0. 지금 당장 해야 할 것은... url으로 계속 접속해 들어가서 내가 원하는 정보들을 끌어올 수 있는지! 

최종목표는 pandas을 사용해서 표로 만드는 것이다!

taskClcd이게 물품 공사 외주 등등
물품은 값이 1이다.
나중에 최적화할 때 사용할 수 있을 것이다. 

response으로 다시 했을 때 값이 8081

와 이거 모르겠다. 머리가 안돌아가네 ㅋㅋ
무슨 포트 번호로 요청을 다르게 하는 것 같다.
다른 포트로 다른 프로세스로 실행하는 듯. 
부하 분산을 줄이기 위해서?

아무튼 아까 갔던 그 포트를 사용하고, 
공고번호를 이용해서 접속한다면 되지 않을까?


포트번호가 어떤 경우에 어떻게 나오는지 파악을 해야 할 것 같다.




## curl try

{'bidno': '20160514664', 'bidseq': '00', 'bidcate' : '0', 'rebidno': '0', 'progressInfo':'개찰완료'},
```
curl -d "bidno=20160514664&bidseq=00&bidcate=0&rebidno=0&progressInfo=%B0%B3%C2%FB%BF%CF%B7%E1" \
-H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36" \
-H "Origin: http://www.g2b.go.kr:8081" \
-H "Content-Type: application/x-www-form-urlencoded" \
-H "Referer: http://www.g2b.go.kr:8081/" \
-X POST http://www.g2b.go.kr:8101/ep/result/facilBidResultDtl.do | iconv -c -f euc-kr -t utf-8 > output.xml
```
되앤다~~~~~~~

* utf-8으로 바꾸기
iconv -c -f euc-kr -t utf-8 > output.xml

다른 공고로 다시 시도

```
<a class="btn_mdl" href="javascript:toDetail('1', '20210105312', '00', '1', '0', '개찰완료');"><span>개찰완료</span></a>
```

```
curl -d "bidno=20210105312&bidseq=00&bidcate=1&rebidno=0&progressInfo=%B0%B3%C2%FB%BF%CF%B7%E1" \
-H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36" \
-H "Origin: http://www.g2b.go.kr:8081" \
-H "Content-Type: application/x-www-form-urlencoded" \
-H "Referer: http://www.g2b.go.kr:8081/" \
-X POST http://www.g2b.go.kr:8101/ep/result/prodBidResultDtl.do | iconv -c -f euc-kr -t utf-8 > output.xml
```

이전에 안되었던 이유는... 사실 인코딩 문제였다... 개찰완료를 string으로 전달하는데 나는 계속 한글로 개찰완료로 쳐서 보냈었는데 아마 나는 utf-8으로 되어있고.
그런데 jsp로 만든 이 웹 앱은 euc-kr이다... 그리고 개발자가 만든 환경이 아니면 잘못된 접근이라고 에러처리를 해뒀던 모양이다.

만약에 헤더가 없으면?
```
curl -d "bidno=20160514664&bidseq=00&bidcate=0&rebidno=0&progressInfo=%B0%B3%C2%FB%BF%CF%B7%E1" \
-X POST http://www.g2b.go.kr:8101/ep/result/facilBidResultDtl.do | iconv -c -f euc-kr -t utf-8
```

* 이제 다시 스크래피로 돌아가서 자동화하자
* https://docs.scrapy.org/en/latest/topics/request-response.html
을 보고 form reqeust 가 아니라 일반 request에서 method = post으로 header 설정해서 요청을 보내자.

그냥 formRequest을 해보니까 다시 비정상적인 연결이라고 나온다.



## scrapy 요령
scrapy.Request는 스크래피에서 사용하는 일반적인 request함수이다. 그냥 html과 xml파일을 요청해서 받는 일반적인 get request이다. 물론 함수 인자를 통해서 post를 사용할 수도 있다. scrapy.request는 python의 기본 request을 활용해서 만든 라이브러리이다.

그리고 request을 보내는 한가지 요령은 크롬에서 private 모드로 해당 사이트로 들어가서 개발자 모드 - > 네트워크에서 응답 함수를 확인해보는 것이다.
지금 같은 경우는 javascript으로 동적으로 데이터를 받아오는 경우였다. 이 경우 해당 자바스크립트 함수를 파악하면 도움이 된다. 
개발자모드에서 element에서 글자 찾기 ctr f을 사용하자!



## 해결한 코드!
```
        done="개찰완료".encode('euc-kr')

        payload={'bidno': '20160514664', 'bidseq': '00', 'bidcate' : '0', 'rebidno': '0', 'progressInfo':done }
        yield scrapy.Request(url = start_url, method="POST", body=json.dumps(payload),callback = self.parse
```

아니 도대체 뭐가 됐다는거야. 다시 에러 나면서 안되는데.

post에 body을 안넣기도 하고... json.dump으로 해서 fs을 지정하라는 말을 듣기도 했지만... 우여곡절 긑에 가져오기 성공!

그런데 지금 한가지 문제는... 지금 scrapy의 문제는 동적 페이지를 못가져온다는 것! 그래서 공식 문서에서도 동적 문서에 해당하는 페이지 주소를 다시 받아서 사용하라고 하고 있다!
selenium과 scrapy을 연결하면 동적페이지도 할 수 있다고 한다!

scrapy의 장점은 middleware와 item 클래스를 활용해 DB으로 쉽제 저장할 수 있다는 것!

그럼 일단 어차피 동적 페이지를 계속 끌고 와야 하니까 selenium과 scrapy을 합친 프로젝트를 참조해보자!

## 나중에 자동으로 찾을 때 사용할 코드
```
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

        
```

그래서 selenium을 사용했다. 잘 가지고 온다... 너무 고생...

middleware에서 내용을 추가하고
spider에서 middleware을 사용한다고 설정했다.
spider에서 기본 약식 형태를 사용

이제 tr을 pandas으로 자동으로 변환할 수 있는지 알아보자.

pandas.read_html을 통해서 바로 추출해낼 수 있다.

이제 1개의 공고에 대해서 데이터를 추출해낼 수 있으니 다수의 공고에 대해서 데이터를 추출해보자!

최근 3달까지 검색이 가능하다. 
그리고 다음 페이지 버튼이 있다. 
각 페이지에는 각 공고들이 있다.

각 페이지에서 각 공고들의 url을 모두 수집한다.

이것을 모든 페이지에 반복한다.

그러면 3달짜리의 모든 url을 수집할 수 있다. 각 url만 있으면 지금까지 한 것들을 반복문을 반복.




## 자동화를 위한 url 진입 구조
3개월 경기도 검색 결과
http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?taskClCds=&bidNm=%B5%B5%BC%AD&searchDtType=1&fromBidDt=2016/04/15&toBidDt=2016/05/15&fromOpenBidDt=&toOpenBidDt=&radOrgan=1&instNm=&area=&regYn=Y&bidSearchType=1&searchType=1

2016 04 15 부터 2016 05 15까지다.

이걸 최근으로 바꿔보자
http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?taskClCds=&bidNm=%B5%B5%BC%AD&searchDtType=1&fromBidDt=2020/11/01&toBidDt=2020/12/01&fromOpenBidDt=&toOpenBidDt=&radOrgan=1&instNm=&area=&regYn=Y&bidSearchType=1&searchType=1

여기에서 링크를 수집.

그런데 수집할 때... 업무가 물품

개찰완료 버튼
나에게 필요한 정보는... 공고번호!가 아니라... 어차피 클릭으로 할 것이니까...

의사코드
```
start_url = [...]

scrapy request

parse
	
```



지금 상황

selenium으로 바꾸고 나서 ... 검색을 할 수 있다.
각 페이지가 나오면 특정 페이지의 공고로 가서 pandas을 이용해서 해당 데이터를 뽑을 수 있다.

문제점 : 동시에 안된다. 
하려면 이전 페이지로 돌아와서 다시 해야 한다...

동적으로 하려면? 
scrapy와 selenium을 같이 사용할 수 있을까?

함수 마다 다른 미들웨어를 사용할 수 있을까?


만약에 1년치의 결과를 한꺼번에 추출한다면? 
일단 12개의 페이지가 있어야 한다.
이걸 동시에 어떻게? 

페이지를 12개를 연다. 
각 페이지를... 보낸다. selenium으로.
selenium에서 그걸 한다. 그게 뭐지? 그 그'
form을 입력해서 click search

한 response에서... 몇개의 공고가 나온다. 
각 공고를... 다시 selenium으로 보낸다. 동적 페이지를 연다. 
각 세부 공고 페이지를 pandans으로 연다. 

즉 2개의 selenium을 사용해야 한다. 

middleware downloader 함수를 하나 더 만들어서
각 함수 안에 끼워넣는다면?

3개월 씩 보내서...
3개월 짜리 1개를 보냈다고 하자. 
그럼 값이 나온다. 
그리고... ? 
페이지가 나온다. 그러면?

거기에서 다시 1개씩... 받는다. url만 따오면 된다. 그냥 스크립트로 짜면?
web driver가... 그... multithreading에 대해서 의도하는대로 안된다고 한다...

그래서 어떻게? 

그러면... 다시... 그 공고번호를 다 알아내어서
form request을 만들어서 검색?

## 의사코드 정리

* 접근 가능한 사이트 경로를 먼저 파악해보자.
  * 검색 form 입력 화면
    * 공고번호와 개찰완료 버튼들
    * 개찰완료 버튼을 누르면 목적 페이지가 나타난다.
  * 공고 번호를 알면 목적 페이지로 바로 접근할 수 있다.


* 가능한 경로 파악
  * 검색 form 화면 -> selenium으로 검색 버튼 클릭 -> 공고 번호 수집 -> form requset
  * 검색 form 화면 -> selenium으로 검색 버튼 클릭 -> 개찰완료 버튼

* 두번째 방법의 문제점
  * 검색 완료 페이지에서 하나의 공고로 들어간 뒤에 다시 뒤로 빠져나온 다음에 다시 기존의 검색 결과 페이지로 돌아간 다음 다른 공고로 들어가야 한다. 그런데 문제는 검색 결과 페이지 역시 동적으로 불러온 사이트이기 때문에... 사이트 번호를 url을 다시... 돌아가서... sequential하게 움직일 뿐더러...
* 첫번째 방법을 해보자
검색 화면에서 selenium으로 검색어를 입력한다. 다음에 나온 화면에서 공고번호를 다 딴다. 조건은 개찰완료인 상태여야 한다.
그리고 그냥 javascript 인자 내용을 그대로 받자. 그리고 그 결과를 파싱해서 scrapy requset을 보낸다. 이 부분은 paralel하게 할 수 있다. 각 함수에서 table을 수집한다.


의사코드
```
import scrapy and selenium

url = 검색 입력 페이지

tables=[]

start_requset
	selenium driver init
	user driver to form inputs
	click search button

	ans_list
	for i = 0 to table length
		if state = 개찰완료
			ans_list.append(row_javascript_arguments)
	
	for i in ans_list
		scrapy.requset(row_javascript_arguments, callback=cumulate)

cummulate(response)
	tb=pandas.read_html(response.html)

	tables.append(tb)
	
```






scrapy와 selenium을 결합할 것이다. scrapy에서 1번의 middleware을 사용할 수 있다. 



이제 내가 해야 하는 것? 

지금 나라장터에 우리가 사용하고 싶은 페이지는 자바스크립트로 동적으로 가지고 온다. 그리고 또... 꼭 필요한 인자를 한글로 전달한다. 게다가... 나라장터는 한글 인코딩이 euc-kr으로 되어있다(charset = euc-kr). 문제는... scrapy에서 평행적으로 실행하려면... json.dump으로 post body dictionary을 string으로 바꿔야 한다. 그런데 json.dump가 버그로 인해서 이제 바이트 코드를 받아주지 않는다! JSON serialized ... 뭐 이런 에러를 뿜는다. 오랫동안 검색을 해봤으나... 해답을 못찾았다. 그래서 그냥... 평행적으로 하는 것을 포기하고... sequential하게 뽑기로 했다. 어쩔 수 없음... 

유니코드 : 모든 언어 문자에 대해 매핑한 정수 코드. 보통 그래서 기준이 된다. 파이썬은 모든 string을 유니코드로 인식한다. 
바이트코드 : 유니코드를 다른 정수 코드로 바꿔진 코드. 바이트로 쓴다. \x....은 16진법으로 매핑된 문자. 특정 유니코드가 이 바이트 코드로 매핑되는 것.
encode : 유니코드를 바이트코드로 정수화 암호화하는 것. 
decode : 바이트코드를 다시 유니코드로 푸는 것. 