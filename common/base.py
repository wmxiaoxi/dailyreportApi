import requests

from common.con_sql import InceptorConnect



headers={"Content-Type":"application/json",
           "Accept-Encoding":"br, gzip, deflate,UTF-8",
            "Connection":"keep-alive",
            "Accept":"*/*",
            "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.12(0x17000c2d) NetType/WIFI Language/zh_CN",
            "Referer":"https://servicewechat.com/wxf8819fa5cf083a6e/0/page-frame.html",
            "Accept-Language":"zh-cn",
            "Host":"dailyminiapp.hugeleafdata.com"}
def sd(classification,datatype,searchWord,url):
    n=0
    count=1
    list=[]
    j=0
    while count!=0:
        n=n+1
        body = {"searchWord": searchWord, "intervalDateType": datatype, "page": n, "rows": 10, "classification":classification}
        req = requests.post(url=url, json=body, headers=headers)
        result = req.json()
        count = len((result["content"]))
        j=count+j
        list.append(count)
    #print(list)
    return j

def sqlcheck(sql):
    # ###连接postgresql
    sql=sql
    newpg=InceptorConnect()
    newpgcoon=newpg.postgconnect()
    sqlresult=newpg.get_all_data(newpgcoon,sql)
    sqlcount=len(sqlresult)
    return sqlcount


##含有的内容
def new(classfication,param):
    value="select" +param+" from public.data_daily where classification='"+classfication+"' and date between current_date - interval '6 day' and current_date limit 1"
    newpg = InceptorConnect()
    newpgcoon = newpg.postgconnect()
    sqlresult = newpg.get_all_data(newpgcoon, value)
    #print(sqlresult)
    if sqlresult==[]:
        return sqlresult
    else:
        return sqlresult[0][0][0:2]



