import allure
import pytest
import time
from common.base import *
class Test_peroidcheck():
    url= "http://192.168.17.212:10021/dataDaily/getDataDailyForPc"
    headers = {"Content-Type": "application/json",
               "Accept-Encoding": "br, gzip, deflate,UTF-8",
               "Connection": "keep-alive",
               "Accept": "*/*",
               "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.12(0x17000c2d) NetType/WIFI Language/zh_CN",
               "Referer": "https://servicewechat.com/wxf8819fa5cf083a6e/0/page-frame.html",
               "Accept-Language": "zh-cn",
               "Host": "dailyminiapp.hugeleafdata.com"}

    def sd1(self,classification, searchWord):
        n = 0
        count = 1
        list = []
        j = 0
        while count != 0:
            n = n + 1
            body = {"searchWord": searchWord,  "page": n, "rows": 10,
                    "classification": classification}
            req = requests.post(url=self.url,json=body, headers=self.headers)
            result = req.json()
            count = len((result["content"]))
            j = count + j
            list.append(count)
        # print(list)
        return j


    @pytest.mark.parametrize('classfication',['行业动态',"收视率",'网络热度','新词热梗','上新影视','一周电影速览'])
    def test_01(self,classfication):
        key='海淀法院公布'
        res1=self.sd1(classfication,key)
        if classfication=='网络热度':
            sql = "select * from (select * from public.data_daily where classification='" + classfication + "' and date between  '2020-05-05' and '2020-05-18')   aa where  aa.title like '" + key + "%' or aa.target like '%"+key+"%'"
            print(sql)
            res2=sqlcheck(sql)
        elif  classfication=='收视率':
            sql = "select * from (select * from public.data_daily where classification='" + classfication + "' and  date between  '2020-05-05' and '2020-05-18')   aa where  aa.title like '%" + key + "%' or aa.target like '%" + key + "%'"
            print(sql)
            res2 = sqlcheck(sql)
        else:
            sql = "select * from (select * from public.data_daily where classification='" + classfication + "' and  date between   '2020-05-05' and '2020-05-18')   aa where  aa.title like '%" + key + "%' or aa.target like '%" + key + "%' or aa.content like '%" + key + "%'"
            print(sql)
            res2 = sqlcheck(sql)
        assert res1==res2

if __name__=="__main__":
    #pytest.main(['-s','test_modify.py','--reruns','2','--reruns-delay','3'])
    pytest.main(['-s', 'test_periodtime.py'])

