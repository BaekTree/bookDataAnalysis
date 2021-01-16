
var request = require('request');

var url = 'http://apis.data.go.kr/1230000/ScsbidInfoService/getOpengResultListInfoThngPreparPcDetail';
var queryParams = '?' + encodeURIComponent('ServiceKey') + '=서비스키'; /* Service Key*/
queryParams += '&' + encodeURIComponent('numOfRows') + '=' + encodeURIComponent('10'); /* */
queryParams += '&' + encodeURIComponent('pageNo') + '=' + encodeURIComponent('1'); /* */
queryParams += '&' + encodeURIComponent('inqryDiv') + '=' + encodeURIComponent('1'); /* */
queryParams += '&' + encodeURIComponent('inqryBgnDt') + '=' + encodeURIComponent('201605010000'); /* */
queryParams += '&' + encodeURIComponent('inqryEndDt') + '=' + encodeURIComponent('201605052359'); /* */
queryParams += '&' + encodeURIComponent('bidNtceNo') + '=' + encodeURIComponent('20130715059'); /* */
queryParams += '&' + encodeURIComponent('type') + '=' + encodeURIComponent('json'); /* */

request({
    url: url + queryParams,
    method: 'GET'
}, function (error, response, body) {
    //console.log('Status', response.statusCode);
    //console.log('Headers', JSON.stringify(response.headers));
    //console.log('Reponse received', body);
});
