import pymysql
# 클래스 선언
class DBConnect:
    # 생성자 선언
    def __init__(self):
        # MySQL DB와 연결을 위한 connect 인스턴스를 선언
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='jja', charset='utf8')
        # 파이썬에서 쿼리를 사용하고 저장하기 위한 cursor 인스턴스 선언
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)

    # 간단한 insert 메서드 정의
    def insert(self, title, contents, category, field, FinishDate, URL, PostDate):
        try:
            # insert 쿼리 작성
            sql = "INSERT INTO RECRUIT VALUES (%s,'1','ss',%s,%s,%s, %s,%s,%s)"
            val = (category, field,title, contents, FinishDate, URL, PostDate)

            self.curs.execute(sql, val)
            # DML문 완료 후 커밋
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
        # 커넥트 인스턴스를 닫아준다.
            self.conn.close()