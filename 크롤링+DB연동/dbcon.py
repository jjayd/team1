import pymysql
from datetime import datetime
from search_craw import Search
# 클래스 선언
class DBConnect:
    # 생성자 선언
    def __init__(self):
        # MySQL DB와 연결을 위한 connect 인스턴스를 선언
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='jja', charset='utf8')
        # 파이썬에서 쿼리를 사용하고 저장하기 위한 cursor 인스턴스 선언
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
    #db 자료 분류
    def make(self, field, title, contents, URL):
        sc = Search
        cate = sc.category(title)
        if cate == "취업":
            category = 1
        elif cate == "인턴":
            category = 2
        else:
            category = 3

        if category != 3:
            (num1, num2, num3, num4) = sc.period(contents)
            year = datetime.today().year
            FinishDate = str(year) + "-" + str(num3) + "-" + str(num4)
            PostDate = str(datetime.today().year) + "-" + str(datetime.today().month) + "-" + str(datetime.today().day)
            self.insert(title, contents, category, field, FinishDate, URL, PostDate)
    # 간단한 insert 메서드 정의
    def insert(self, title, contents, category, field, FinishDate, URL, PostDate):
        try:
            # insert 쿼리 작성
            if category == 1:
                qry = "SELECT MAX(RNO) FROM RECRUIT WHERE CNO=1;"
            else:
                qry = "SELECT MAX(RNO) FROM RECRUIT WHERE CNO=2;"
            self.curs.execute(qry)
            result = self.curs.fetchone()
            print(result['MAX(RNO)'])
            if str(result['MAX(RNO)']) == 'None':
                rno = 1
            else:
                rno = int(result['MAX(RNO)']) + 1
            sql = "INSERT INTO RECRUIT VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (category, rno, field, title, contents, FinishDate, URL, PostDate)
            print(val)
            self.curs.execute(sql, val)
            # DML문 완료 후 커밋
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
        # 커넥트 인스턴스를 닫아준다.
            self.conn.close()