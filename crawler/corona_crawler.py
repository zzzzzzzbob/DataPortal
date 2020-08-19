from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from datetime import datetime as dt


from control_mongo import to_mongo
# to_mongo.insert_data(data, dest)

DATA_URL = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun="

class Corona:
    def __init__ (self):
        self.data = requests.get(DATA_URL)
        self.corona_data = pd.read_html(self.data.content, encoding="utf8")
    
    # 누적 확진자 현황
    def confirmed_cases(self):
        pass
    
    # 누적 검사 현황
    def testing_in_korea(self):
        dataset = {}
        testing_data = self.corona_data[1]
        for d in testing_data:
            
            # dataset initialize
            if d[0] not in dataset:
                dataset[d[0]] = {}

            # numpy.int64 -> int 필요

            # 검사중, 합계
            if d[0] == d[1] == d[2]:
                dataset[d[0]] = testing_data[d][0].item()

            # 검사완료 -> 결과음성, 소계
            elif d[0] != d[1] and d[1] == d[2]:
                print(d)
                if d[1] not in dataset[d[0]] :
                    dataset[d[0]][d[1]] = testing_data[d][0].item()

            # 검사완료 -> 확진환자수 -> 격리중, 격리해제, 사망, 소계
            else:
                if d[1] not in dataset[d[0]] :
                    dataset[d[0]][d[1]] = {}
                    dataset[d[0]][d[1]][d[2]] = testing_data[d][0].item()
                else:
                    dataset[d[0]][d[1]][d[2]] = testing_data[d][0].item()
                
        return {"누적검사현황" : dataset}

    # 해외유입 환자현황
    def imported_cases(self):

        # 해외유입 환자현황 데이터 세팅
        k = self.corona_data[0].loc[:,['구분.1', '신규', '누계']]
        dataset = {}
        for idx in range(len(k)):
            # pandas 의 int 형식의 값은 numpy.int 로 몽고에 insert하게되면 타입 에러 발생 --> item() 을 통하여 int로 변경
            dataset[k.iloc[idx]['구분.1']] = {"신규": k.iloc[idx]['신규'].item(), "누계" : k.loc[idx]['누계'].item()}
                
        return {"해외유입환자현황":dataset}

    def get_and_insert_data(self):
        sum_dataset = {}
        
        # sum_dataset.update(self.confirmed_cases())
        sum_dataset.update(self.testing_in_korea())
        sum_dataset.update(self.imported_cases())
        
        mg = to_mongo()
        mg.insert_data({dt.date(dt.now()).isoformat():sum_dataset}, 'corona_data')

if __name__ == "__main__":
    crawler = Corona()
    crawler.get_and_insert_data()
    print("# Done")