import allure
import pytest
import time
from common.base import *
class Test_check():
    url = 'https://dailyminiapp.hugeleafdata.com/dataDaily/getDataDailyForMobile'
    datatype = 'sevenDay'
    @allure.story("类型+最近7天+内容查询--输入的是个标题，查询出内容/标签/标题中含有内容的数据")
    @pytest.mark.parametrize('classfication',['行业动态',"收视率",'网络热度','新词热梗','上新影视','一周电影速览'])
    def test_01(self,classfication):
        key=new(classfication,' title')
        print(key)
        time.sleep(1)

        if key!=[]:
            res1 = sd(classfication, self.datatype, key, self.url)
            if classfication=='网络热度':
                sql = "select aa.title,aa.target,aa.content from (select * from public.data_daily where classification='" + classfication + "' and date between current_date - interval '6 day' and current_date)   aa where  aa.title like '%" + key + "%' or aa.target like '%"+key+"%'"
                print(sql)
                res2=sqlcheck(sql)
            elif  classfication=='收视率':
                sql = "select aa.title,aa.target,aa.content from (select * from public.data_daily where classification='" + classfication + "' and date between current_date - interval '6 day' and current_date)   aa where  aa.title like '%" + key + "%' or aa.target like '%" + key + "%'"
                print(sql)
                res2 = sqlcheck(sql)
            else:
                sql = "select aa.title,aa.target,aa.content from (select * from public.data_daily where classification='" + classfication + "' and date between current_date - interval '6 day' and current_date)   aa where  aa.title like '%" + key + "%' or aa.target like '%" + key + "%' or aa.content like '%" + key + "%'"
                print(sql)
                res2 = sqlcheck(sql)
            assert res1==res2

        else:
            res1=0
            sql = "select * from public.data_daily where classification='" + classfication + "' and date between current_date - interval '6 day' and current_date"
            res2 = sqlcheck(sql)
            assert res1==res2




    @allure.story("类型+最近7天+内容查询--输入的是个内容存在关键字，查询出内容/标签/标题中含有内容的数据")
    @pytest.mark.parametrize('classfication',['行业动态','新词热梗','上新影视','一周电影速览'])
    def test_02(self,classfication):
        key=new(classfication,' content')
        print(key)
        time.sleep(1)

        if key!=[]:
            res1 = sd(classfication, self.datatype, key, self.url)
            sql = "select aa.title,aa.target,aa.content from (select * from public.data_daily where classification='" + classfication + "' and date between current_date - interval '6 day' and current_date)   aa where  aa.title like '%" + key + "%' or aa.target like '%"+key+"%' or aa.content like '%"+key+"%'"
            print(sql)
            res2=sqlcheck(sql)
            assert res1==res2

        else:
            res1=0
            sql = "select * from public.data_daily where classification='" + classfication + "' and date between current_date - interval '6 day' and current_date"
            res2 = sqlcheck(sql)
            assert res1==res2






    @allure.story("类型+最近7天+内容查询--输入的是个标签存在关键字，查询出内容/标签/标题中含有内容的数据")
    @pytest.mark.parametrize('classfication', ['行业动态', "收视率", '网络热度', '新词热梗', '上新影视', '一周电影速览'])
    def test_03(self, classfication):
        key = new(classfication, ' target')
        print(key)
        time.sleep(1)

        if key != []:
            res1 = sd(classfication, self.datatype, key, self.url)
            if classfication == '网络热度':
                sql = "select aa.title,aa.target,aa.content from (select * from public.data_daily where classification='" + classfication + "' and date between current_date - interval '6 day' and current_date)   aa where  aa.title like '%" + key + "%' or aa.target like '%" + key + "%'"
                print(sql)
                res2 = sqlcheck(sql)
            elif classfication == '收视率':
                sql = "select aa.title,aa.target,aa.content from (select * from public.data_daily where classification='" + classfication + "' and date between current_date - interval '6 day' and current_date)   aa where  aa.title like '%" + key + "%' or aa.target like '%" + key + "%'"
                print(sql)
                res2 = sqlcheck(sql)
            else:
                sql = "select aa.title,aa.target,aa.content from (select * from public.data_daily where classification='" + classfication + "' and date between current_date - interval '6 day' and current_date)   aa where  aa.title like '%" + key + "%' or aa.target like '%" + key + "%' or aa.content like '%" + key + "%'"
                print(sql)
                res2 = sqlcheck(sql)
            assert  res1==res2

        else:
            res1=0
            sql = "select * from public.data_daily where classification='" + classfication + "' and date between current_date - interval '6 day' and current_date"
            res2 = sqlcheck(sql)
            assert res1 == res2

if __name__=="__main__":
    #pytest.main(['-s','test_modify.py','--reruns','2','--reruns-delay','3'])
    pytest.main(['-s', 'test_check.py'])

