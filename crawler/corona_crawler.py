from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from datetime import datetime as dt


from control_mongo import to_mongo
# to_mongo.insert_data(data, dest)

data = requests.get("http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun=")
corona_data = pd.read_html(data.content, encoding="utf8")

# 해외유입 환자현황 데이터 세팅
k = corona_data[0].loc[:,['구분.1', '신규', '누계']]
data_set = {}
data_sub_set = {}
for idx in range(len(k)):
    # pandas 의 int 형식의 값은 numpy.int 로 몽고에 insert하게되면 타입 에러 발생 --> item() 으로 대체
    
    data_sub_set[k.iloc[idx]['구분.1']] = {"신규": k.iloc[idx]['신규'].item(), "누계" : k.loc[idx]['누계'].item()}
#     print("국가 : {}, 수량 : {}".format(k.iloc[idx]['구분.1'], k.iloc[idx]["신규"]))
data_set[dt.date(dt.now()).isoformat()] = data_sub_set

# print(data_set)
# Data insert to mongo
mg = to_mongo()
mg.insert_data(data_set, 'corona_data')
