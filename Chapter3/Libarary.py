#표준 라이브러리
# "도서관"이라는 듯 그대로 원하는 정보를 찾아보는 곳이다.
# 모든 라이브러리는 다 알 필요는 없고, 어떤 일을 할 때 어떤 라이브러리를 사용해야는 정도만 알아두자
# 자주 사용되고 꼭 알아 두면 좋은 라이브러리를 중심으로 보자
#  >파이썬 표준 라이브러리는 파이썬을 설치할 때 자동으로 컴퓨터에 설치됨
#  >sys,re모듈은 파이썬의 중요한 표준 라이브러리이다.

#datetime.date
# 년,월,일로 날짜를 표현할 때 사용하는 함수이다.
#datetime.date는 다음과 같이 객체로 만들 수 있다.
import datetime
day1 = datetime.date(2021,12,14)
day2 = datetime.date(2022,6,12)

diff = day2 - day1
print(diff.days)

print(day1.weekday())