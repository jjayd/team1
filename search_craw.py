# -*- coding: utf-8 -*-
from datetime import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# 클래스 선언
class Search:
    # 기간 구하는 메서드 정의
    def period(self, str):
        try:
            str=str.replace(" ", "")
            year = datetime.today().year
            offset = str.find("일정")
            if offset == -1:
                offset = str.find("일시")
            if offset == -1 :
                offset = str.find("기간")
            if offset == -1:
                offset = str.find("기한")
            if offset == -1 :
                offset = str.find("접수일")
            start = offset

            #1 x월 x일 ~ x월 x일
            offset = str.find("월",start,start+15)

            if offset != -1 :
                offset2 =str.find("일",offset,offset+5)
                if offset2 != -1 :
                    if str[offset - 2] == '1' :
                        data = int(str[offset-1])+10
                    else :
                        data = int(str[offset-1])
                    if str[offset2 - 2] == '1' or str[offset2 - 2] == '2' or str[offset2 - 2] == '3':
                        data2 = int(str[offset2 - 1]) + int(str[offset2 - 2])*10
                    else :
                        data2 = int(str[offset2-1])

                else:
                    if str[offset - 2] == '1' :
                        data = int(str[offset-1])+10
                    else :
                        data = int(str[offset-1])
                    data2 = 0

                offset = str.find("~", offset2, offset2 + 15)
                if offset == -1:
                    offset = str.find("부터", offset2, offset2 + 15)
                if offset == -1:
                    offset = str.find("-", offset2, offset2 + 15)
                offset2 = offset
                offset = str.find("월", offset)

                if offset != -1:
                    offset2 = str.find("일", offset, offset + 5)
                    if offset2 != -1:
                        if str[offset - 2] == '1':
                            data3 = int(str[offset - 1]) + 10
                        else:
                            data3 = int(str[offset - 1])
                        if str[offset2 - 2] == '1' or str[offset2 - 2] == '2' or str[offset2 - 2] == '3':
                            data4 = int(str[offset2 - 1]) + int(str[offset2 - 2]) * 10
                        else:
                            data4 = int(str[offset2 - 1])
                        return (data, data2, data3, data4)
                    else:
                        if str[offset - 2] == '1':
                            data3 = int(str[offset - 1]) + 10
                        else:
                            data3 = int(str[offset - 1])
                        data4 = 0
                        return (data, data2, data3, data4)
                else:
                    offset2 = str.find("일", offset2, offset2 + 5)
                    if offset2 != -1:
                        if str[offset2 - 2] == '1' or str[offset2 - 2] == '2' or str[offset2 - 2] == '3':
                            data4 = int(str[offset2 - 1]) + int(str[offset2 - 2]) * 10
                        else:
                            data4 = int(str[offset2 - 1])
                        data3 = 0
                        return (data, data2, data3, data4)
                    else:
                        data3 = 0
                        data4 = 0
                        return (data, data2, data3, data4)
            else :
                data = 0
                data2 = 0

            #2 x/x ~ x/x
            offset = str.find("/", start,start+15)

            if offset != -1 :
                    if str[offset - 2] == '1' :
                        data = int(str[offset-1])+10
                    else :
                        data = int(str[offset-1])
                    if int(str[offset + 2]) >=0 and int(str[offset + 2]) <=9 :
                        data2 = int(str[offset + 2]) + int(str[offset + 1])*10
                    else :
                        data2 = int(str[offset+1])
                    offset = str.find("~", offset, offset + 15)
                    if offset == -1:
                        offset = str.find("부터", offset, offset + 15)
                    if offset == -1:
                        offset = str.find("-", offset, offset + 15)

                    offset = str.find("/", offset)
                    if offset != -1:
                        if str[offset - 2] == '1':
                            data3 = int(str[offset - 1]) + 10
                        else:
                            data3 = int(str[offset - 1])
                        if str[offset + 2] > '0' and str[offset + 2] <= '9':
                            data4 = int(str[offset + 2]) + int(str[offset + 1]) * 10
                        else:
                            data4 = int(str[offset + 1])
                        return (data, data2, data3, data4)
                    else:
                        data3 = 0
                        data4 = 0
                        return (data, data2, data3, data4)
            else :
                data = 0
                data2 = 0


            #3 x.x ~ x.x
            offset = str.find(".", start,start+15)

            if offset != -1:
                if str[offset -4] == '2' and str[offset-3] == '0':
                    offset = str.find(".", offset+1)
                    if str[offset - 2] == '1':
                        data = int(str[offset - 1]) + 10
                    else:
                        data = int(str[offset - 1])
                    if int(str[offset + 2]) >= 0 and int(str[offset + 2]) <= 9:
                        data2 = int(str[offset + 2]) + int(str[offset + 1]) * 10
                    else:
                        data2 = int(str[offset + 1])
                else:
                    if str[offset - 2] == '1':
                        data = int(str[offset - 1]) + 10
                    else:
                        data = int(str[offset - 1])
                    if int(str[offset + 2]) >= 0 and int(str[offset + 2]) <= 9:
                        data2 = int(str[offset + 2]) + int(str[offset + 1]) * 10
                    else:
                        data2 = int(str[offset + 1])
                offset = str.find("~", offset, offset + 15)
                if offset == -1:
                    offset = str.find("부터", offset, offset + 15)
                if offset == -1:
                    offset = str.find("-", offset, offset + 15)

                offset = str.find(".", offset)

                if offset != -1:
                    if str[offset - 4] == '2' and str[offset - 3] == '0':
                        offset = str.find(".", offset + 1)
                        if str[offset - 2] == '1':
                            data3 = int(str[offset - 1]) + 10
                        else:
                            data3 = int(str[offset - 1])
                        if int(str[offset + 2]) >= 0 and int(str[offset + 2]) <= 9:
                            data4 = int(str[offset + 2]) + int(str[offset + 1]) * 10
                        else:
                            data4 = int(str[offset + 1])
                        return (data, data2, data3, data4)
                    else:
                        if str[offset - 2] == '1':
                            data3 = int(str[offset - 1]) + 10
                        else:
                            data3 = int(str[offset - 1])
                        if int(str[offset + 2]) >= 0 and int(str[offset + 2]) <= 9:
                            data4 = int(str[offset + 2]) + int(str[offset + 1]) * 10
                        else:
                            data4 = int(str[offset + 1])
                        return (data, data2, data3, data4)
                else:
                    data3 = 0
                    data4 = 0
                    return (data, data2, data3, data4)
            else:
                data = 0
                data2 = 0
                data3 = 0
                data4 = 0
                return (data, data2, data3, data4)
        except:
            data = 0
            data2 = 0
            data3 = 0
            data4 = 0
            return (data, data2, data3, data4)

    #카테고리 구하는 메서드 정의
    def category(self, str):
        if str.find("인턴") != -1 or str.find("internship") != -1 :
            return "인턴"
        elif str.find("채용") != -1 or str.find("신입사원") != -1 or str.find("인재모집") != -1 or str.find("공채") != -1:
            return "취업"
        else :
            return "제외"
