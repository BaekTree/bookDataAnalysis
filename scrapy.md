# 스크래피 문서
스파이더를 통해서 크롤링을 해보면 
맨 처음 주소만 잡아주고
나머지는 안잡아준다!

설정에서 robot policy false으로 설정해도 같은 결과

검색 검색...

dynamic loading pages는 안된다고 함.



스크래피로만 시도. soup을 사용하지 않고 해보겠다.

scrapy fetch --nolog 'http://www.g2b.go.kr/pt/menu/selectSubFrame.do?framesrc=/pt/menu/frameTgong.do?url=http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?taskClCds=&bidNm=%B5%B5%BC%AD&searchDtType=1&fromBidDt=2020/12/16&toBidDt=2021/01/15&fromOpenBidDt=&toOpenBidDt=&radOrgan=1&instNm=&area=&regYn=Y&bidSearchType=1&searchType=1' > response.html



1. 해당 페이지에서 반복문으로 각 공고 들어가야 한다. for 사용해서 들어가고, tr[i]으로 조절할 수 있는 것 같다.
여기서 t[10]이 마감이면 그냥 continue으로 다음 index 공고로 보내버리고. 아닌 경우에 진행.
진행 할 때도 마감이 떠 있어야 해당 url으로 접속해서 다음 단계로 진행

0. 지금 당장 해야 할 것은... url으로 계속 접속해 들어가서 내가 원하는 정보들을 끌어올 수 있는지! 

최종목표는 pandas을 사용해서 표로 만드는 것이다!