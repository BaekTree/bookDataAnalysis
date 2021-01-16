// C++ 샘플 코드
using System;
using System.Net;
using System.Net.Http;
using System.IO;

namespace ConsoleApp1
{
    class Program
    {
        static HttpClient client = new HttpClient();
        static void Main(string[] args)
        {
            string url = "http://apis.data.go.kr/1230000/ScsbidInfoService/getOpengResultListInfoThngPreparPcDetail"; // URL
            url += "?ServiceKey=" + "서비스키"; // Service Key
            url += "&numOfRows=10";
            url += "&pageNo=1";
            url += "&inqryDiv=1";
            url += "&inqryBgnDt=201605010000";
            url += "&inqryEndDt=201605052359";
            url += "&bidNtceNo=20130715059";
            url += "&type=json";
            
            var request = (HttpWebRequest)WebRequest.Create(url);
             request.Method = "GET";
            
            string results = string.Empty;
            HttpWebResponse response;
            using (response = request.GetResponse() as HttpWebResponse)
            {
                StreamReader reader = new StreamReader(response.GetResponseStream());
                results = reader.ReadToEnd();
            }
            
            Console.WriteLine(results);
        }
    }
}
