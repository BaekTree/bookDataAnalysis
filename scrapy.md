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

```
 
//<![CDATA[
	function toBidDtl(bidseq){
		var f = document.frmDtl;
		var bidno = f.bidno.value;
		var taskClCd = f.taskClCd.value;
		var popUpYn = f.popUpYn.value;
		location.href="/ep/invitation/publish/bidInfoDtl.do?bidno="+bidno+"&bidseq="+bidseq+"&taskClCd="+taskClCd+"&releaseYn=Y&popUpYn="+popUpYn;
	}
	
	function bidAppendInfo(){
		var f = document.frmDtl;
		var bidno = f.bidno.value;
		var bidseq = f.bidseq.value;
		var taskClCd = f.taskClCd.value;

		var url = '/ep/execution/compete/fwdNomiCompetDataDtlPop.do?nomiPerfClCd=1&bidno='+bidno+'&bidseq='+bidseq;
		popup_openWindowScroll(url, '840', '550', '');
	}
	
	function bidDepositPay(){
		var f = document.frmDtl;
		var bidno = f.bidno.value;
		var bidseq = f.bidseq.value;

		bidLink_payWarr('1', bidno, bidseq);
		//var url = '/ep/join/bidding/listItemBidcate.do?bidno='+bidno+'&bidseq='+bidseq;//입찰보증금 납부결과
		//popup_openWindowScroll(url, '840', '550', '');
	}
	
	function propodocOnlineSrch(bidcate, uiGubun){
		var f = document.frmDtl;
		var bidno = f.bidno.value;
		var bidseq = f.bidseq.value;
		var url = "http://www.g2b.go.kr:8082/ep/execution/eproposal/chkFwdInsertPropoDocFileCont.do"
					+ "?bidno=" + bidno
					+ "&bidseq=" + bidseq
					+ "&bidcate=" + bidcate
					+ "&uiType=Y"
					+ "&uiGubun=" + uiGubun;
		popup_openWindowScroll(url, '840', '550', '');
	}
	
	function baseAmtSrch(){
		var f = document.frmDtl;
		var bidno = f.bidno.value;
		var bidseq = f.bidseq.value;
		var taskClCd = f.taskClCd.value;
		var bidContractMethodCd = f.bidContractMethodCd.value;
		//if(taskClCd == '9')taskClCd='5';
		
		url = "/ep/price/baseamt/selectBaseAmtDtlPopup.do"
				+ "?taskClCd=" + taskClCd
				+ "&bidno=" + bidno
				+ "&bidseq=" + bidseq;
		
		popup_openWindowScroll(url, '840', '550', '');
	}
	
	function jointSppAgtSubmit(type){
		var f = document.frmDtl;
		var bidno = f.bidno.value;
		var bidseq = f.bidseq.value;
		var url;

		if(type == '1'){
			bidLink_rebiddingProd(bidno, bidseq);
		}
		if(type == '2'){//라운드
			goAppActionRound(bidno, bidseq);
		}
		if(type == '3'){//복수경쟁
			bidLink_jointSppAgtProd(bidno, bidseq);
		}
		if(type == '4'){//투찰
			bidLink_jointSppAgtProd(bidno, bidseq);
		}
	}
	
	function feePay(type){
		var f = document.frmDtl;
		var bidno = f.bidno.value;
		var bidseq = f.bidseq.value;
		var url;
		
		if(type == '1'){
			bidLink_rebiddingProd(bidno, bidseq);
		}
		if(type == '2'){
			bidLink_payFee(bidno, ' ');
		}
	}
	
	function reBidding(type){
		if(checkIsOpenPage() == true){
			return;
		}
		
		var f = document.frmDtl;
		var bidno = f.bidno.value;
		var bidseq = f.bidseq.value;
		
		bidLink_rebiddingProd(bidno, bidseq);
	}
	
	function bidding(type){
		if(checkIsOpenPage() == true){
			return;
		}
		
		var f = document.frmDtl;
		var bidno = f.bidno.value;
		var bidseq = f.bidseq.value;
		
		if(type == '1'){//라운드
			bidLink_biddingProd(bidno, bidseq);
		}
	}
	
	function fgprtBidding(){
		if(checkIsOpenPage() == true){
			return;
		}
		
		var f = document.frmDtl;
		var bidno = f.bidno.value;
		var bidseq = f.bidseq.value;
		bidLink_biddingProdAndBidMsg(bidno, bidseq);
	}
	
	function genBidding(){
		if(checkIsOpenPage() == true){
			return;
		}
		
		var f = document.frmDtl;
		var bidno = f.bidno.value;
		var bidseq = f.bidseq.value;
		bidLink_biddingProdAndBidMsg(bidno, bidseq);
	}
	
	function checkIsOpenPage(){
		if('' == 'Y'){
			alert('현재 화면에서 투찰할 수 없습니다.\r\n[입찰정보]-[각업무]-[공고현황]에서 해당 공고 검색 후 투찰하십시오.');
			return true;
		}
		return false;
	}
		
	function bidInfoInit(){
		//
	}
	
	function lawSrch(lawId, joNo,note){
		popup_law('law_001',lawId, joNo, note);	
	}
	
	function prodListExcel(){
		var f = document.frmDtl;
		var bidno = f.bidno.value;
		var bidseq = f.bidseq.value;
		location.href="/ep/invitation/publish/prodListExcel.do?bidno="+bidno+"&bidseq="+bidseq;
	}
	//실적심사 작성
	function perfExamSpec(){
		var f = document.frmDtl;
		var taskClCd = f.taskClCd.value;
		var bidno = f.bidno.value;
		var bidseq = f.bidseq.value;
		//var openbidDtStart 	= f.openBidDt.value;
		//var openbidDtEnd	= f.openBidDt.value;
		var bidDtStart 	= "2021/01/15 17:32".substring(0,10);
		var bidDtEnd	= "2021/01/15 17:32".substring(0,10);
		if(isLogin() == false){
			return;
		}
		var url = "/ep/execution/perfexam/listPagePerfExamBid.do?taskClCd="+taskClCd+"&bidno="+bidno+
					"&bidseq="+bidseq+
					"&bidDtStart="+bidDtStart+
					"&bidDtEnd="+bidDtEnd;
		/*
		var url = "/ep/execution/perfexam/listPagePerfExamReqDoc.do?taskClCd="+taskClCd+"&bidno="+bidno+
					"&bidseq="+bidseq+
					"&openbidDtStart="+openbidDtStart+
					"&openbidDtEnd="+openbidDtEnd;
		*/
		
		location.href=url;
	}
	//적격심사 신청서
	function itemQevalReqDoc(){
		var f = document.frmDtl;
		var bidno = f.bidno.value;
		var bidseq = f.bidseq.value;
		var fromOpenbidYmd 	= f.openBidDt.value;
		var toOpenbidYmd	= f.openBidDt.value;
		var taskClCd = f.taskClCd.value;
		var qevalClCd;
		if(isLogin() == false){
			return;
		}
		
		if(taskClCd == "1"){//물품
			qevalClCd = "1";
		}else if(taskClCd == "9"){//용역
			qevalClCd = "3";
		}else{
			alert("업무구분코드가 없습니다.");
			return;
		}
		
		var url = "http://www.g2b.go.kr:8084/ep/eval/general/qevalTgNtcdocRcvList.do?bidno="+bidno+
				"&qevalClCd="+qevalClCd+
				"&fromOpenbidYmd="+fromOpenbidYmd+
				"&toOpenbidYmd="+toOpenbidYmd;
		location.href=url;
	}
	//기출평가제안서
	function propoDocSumbit(){
		var f = document.frmDtl;
		var bidno = f.bidno.value;
		var bidseq = f.bidseq.value;
		if(isLogin() == false){
			return;
		}
		var url = "/ep/execution/eproposal/listPagePropoDocSubmitBid.do?taskClCd=1&bidno="+bidno+
					"&bidseq="+bidseq;
		
		location.href=url;
	}
	//로그인 체크
	function isLogin(){
		var f = document.frmDtl;
		var loginId = f.loginId.value;
		if(loginId == ''){
			alert('로그인 이후 사용하시기 바랍니다.');
			return false;
		}
		return true;
	}
	function toList(){
		var f = document.frmDtl;
		var url = "javascript:history.go(-1)";
		if(url.indexOf('/ep/tbid/tbidList.do') < 0){
			url = '/ep/tbid/tbidFwd.do?bidSearchType=1';
		}
  		location.href = url;
  	}
	function toMyBidMng(){
		var f = document.frmDtl;
		var bidno = f.bidno.value;
		var bidseq = f.bidseq.value;
		var taskClCd = f.taskClCd.value;
		location.href = "/ep/invitation/mybid/selectMyBidDtl.do?taskClCd="+taskClCd+"&bidno="+bidno+"&bidseq="+bidseq;
	}
	//찜하기
	function toDibsBid(){
		var f = document.frmDtl;
		var bidno = f.bidno.value;
		var bidseq = f.bidseq.value;
		
		var url = '/ep/bidcenter/checkEpDibsBid.do?bidno='+bidno+'&bidseq='+bidseq;
		popup_openWindowScroll(url, '650', '500', 'popup1');
	}
	//표준공고서 보기
	function toBidDocView(){
		var f = document.frmDtl;
  		var bidno			= f.bidno.value;
  		var bidseq			= f.bidseq.value;
  		var taskClCd 		= f.taskClCd.value;
  		var url = "/ep/invitation/publish/bidXmlDocView.do?bidno="+bidno+"&bidseq="+bidseq+"&taskClCd="+taskClCd;
		popup_openWindowScroll(url, 860, 500, 'bidDoc');
	}
	
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

	// 개찰결과 입찰분류 목록 페이지 이동
	function toCateList(taskClCd, bidno, bidseq){
		var cateListUrl = "";
		
		if(taskClCd == "1" || taskClCd == "9"){	// 물품
			cateListUrl = nquryhost + "/ep/result/prodBidResultCateList.do";
		}
		if(taskClCd == "2"){	// 외자
			cateListUrl = nquryhost + "/ep/result/listFrnBidResultCate.do";
		}
		if(taskClCd == "4"){	// 비축
			cateListUrl = nquryhost + "/ep/result/stplBidResultCateList.do";
		}
		if(taskClCd == "6" || taskClCd == "7"){	// 리스
			cateListUrl = nquryhost + "/ep/result/leaseBidResultCateList.do";
		}
		
		document.ebid.bidno.value = bidno;
		document.ebid.bidseq.value = bidseq;
		document.ebid.method = "post";
		document.ebid.action = cateListUrl;
		document.ebid.submit();
		return;
	}
	
	function toBidCenterMain(){
		document.to_main.target = "_self";
		document.to_main.action = "/ep/bidcenter/bidCenterMain.do";
		document.to_main.method = "post";
		document.to_main.submit();
	}
	
	function toDidsBidList(){
		document.to_main.target = "_self";
		document.to_main.action = document.to_main.dibsUrl.value;
		document.to_main.method = "post";
		document.to_main.submit();
	}
	
	function toStdDocEvalResult(){
		var f = document.frmDtl;
		var bidno = f.bidno.value;
		var bidseq = f.bidseq.value;
		var taskClCd = f.taskClCd.value;

		var url = '/ep/execution/techscore/searchStdDocEvalPopup.do?popup=Y&bidno='+bidno+'&bidseq='+bidseq;
		popup_openWindowScroll(url, '840', '550', '');
	}
//]]>

```

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
        yield scrapy.Request(url = start_url, method="POST", body=json.dumps(payload),callback = self.pa
```

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