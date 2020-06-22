import pytest

from common.base import *
import time

class Test_sd():
    url = 'https://dailyminiapp.hugeleafdata.com/dataDaily/getDataDailyForMobile'
    datatype='sevenDay'
    sql_all="select * from public.data_daily where classification!='广电动态' and date between current_date - interval '6 day' and current_date"
    sql_hy="select * from public.data_daily where classification='行业动态' and date between current_date - interval '6 day' and current_date"
    sql_ssl="select * from public.data_daily where classification='收视率' and date between current_date - interval '6 day' and current_date"
    sql_inter = "select * from public.data_daily where classification='网络热度' and date between current_date - interval '6 day' and current_date"
    sql_newword = "select * from public.data_daily where classification='新词热梗' and date between current_date - interval '6 day' and current_date"
    sql_film = "select * from public.data_daily where classification='上新影视' and date between current_date - interval '6 day' and current_date"
    sql_weeklook = "select * from public.data_daily where classification='一周电影速览' and date between current_date - interval '6 day' and current_date"
    @pytest.mark.parametrize('classification,sql',[('行业动态',sql_hy),('收视率',sql_ssl),('网络热度',sql_inter),('新词热梗',sql_newword),('上新影视',sql_film),('一周电影速览',sql_weeklook),('全部',sql_all)])
   #@pytest.mark.parametrize('classification,sql',[('网络热度',sql_ssl)])
    def test_01(self,classification,sql):
        res1=sd(classification,self.datatype,'',self.url)
        res2=sqlcheck(sql)
        assert res1==res2

if __name__=="__main__":
    #pytest.main(['-s','test_sevenday.py','--reruns','2','--reruns-delay','3'])
    pytest.main(['-s', 'test_sevenday.py'])

