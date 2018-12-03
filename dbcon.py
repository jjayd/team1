# -*- coding: utf-8 -*-
import pymysql
from datetime import datetime
from search_craw import Search

# 클래스 선언
class DBConnect:
    # 생성자 선언
    def __init__(self):
        # MySQL DB와 연결을 위한 connect 인스턴스를 선언
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='skku', charset='utf8')
        # 파이썬에서 쿼리를 사용하고 저장하기 위한 cursor 인스턴스 선언
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
    #db 자료 분류
    def make(self, field, title, contents, URL):
        sc = Search()
        cate = sc.category(title)
	print(cate)
        if cate == "취업":
            catego = 1
        elif cate == "인턴":
            catego = 2
        else:
            catego = 3

        if catego != 3:
            (num1, num2, num3, num4) = sc.period(contents)
            year = datetime.today().year
            FinishDate = str(year) + "-" + str(num3) + "-" + str(num4)
            PostDate = str(datetime.today().year) + "-" + str(datetime.today().month) + "-" + str(datetime.today().day)
            print("hoho")
            self.insert(title, contents, catego, field, FinishDate, URL, PostDate)
            
    # 간단한 insert 메서드 정의
    def insert(self, title, contents, category, field, FinishDate, URL, PostDate):
        try:
            # insert 쿼리 작성
            if category == 1:
                qry = "SELECT MAX(RNO) FROM NEW_RECRUIT WHERE CNO=1;"
            else:
                qry = "SELECT MAX(RNO) FROM NEW_RECRUIT WHERE CNO=2;"
            self.curs.execute(qry)
            result = self.curs.fetchone()
            print(result['MAX(RNO)'])
            if str(result['MAX(RNO)']) == 'None':
                rno = 1
            else:
                rno = int(result['MAX(RNO)']) + 1
            JNO=category*1000+rno
            school="성균관대"

            tmp="SET SQL_MODE='ALLOW_INVALID_DATES'"
            self.curs.execute(tmp)

            sql = "INSERT INTO NEW_RECRUIT (CNO,RNO,Field,Title,Contents,FinishDate,URL,PostDate,JNO,school )  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (str(category), rno, field, title, contents, FinishDate, URL, PostDate, JNO, school)
            print(val)
            self.curs.execute(sql, val)
            # DML문 완료 후 커밋
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
        # 커넥트 인스턴스를 닫아준다.
            self.conn.close()
