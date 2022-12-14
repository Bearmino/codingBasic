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

#day2-day1을 뺀 후 diff라는 객체로 리턴 후 days를 사용하여 두 날짜의 차이를 구할 수 있다.
diff = day2 - day1
print(diff.days)
#>>>180

#weekday함수를 통해서 요일을 구할 수 있다.(0부터 월요일시작)
print(day1.weekday())
#>>>1 <-화요일

#weekday함수의 경우 6이 일요일이다. 7을 일요일로 하고 싶은 경우 isoweekday()함수를 사용한다.
print(day1.isoweekday())


#time.time
# time.time()은 UTC(협정 세계 표준시)를 사용하여, 현재 시간을 실수 형태로 리턴하는 함수
import time
print(time.time())

#time.locatime
# time.locatime은 time.time()이 리턴한 실수 값을 사용해서 연도,월,일,시,분,초...의 형태로 바꾸어 주는 함수
lastTime = time.localtime(time.time())
print(lastTime)
#>>> time.struct_time(tm_year=2022, tm_mon=12, tm_mday=14, tm_hour=10, tm_min=27,
# tm_sec=48, tm_wday=2, tm_yday=348, tm_isdst=0)

#time.asctime
# time.localtime에 의해서 반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 리턴하는 함수
lastTime = time.asctime(time.localtime(time.time()))
print(lastTime)
#>>> Wed Dec 14 10:37:32 2022

#time.ctime
# asctime과 다른점은 ctime은 항상 현재 시간만을 리턴하는 함수
lastTime = time.ctime()
print(lastTime)
#>>> Wed Dec 14 10:37:32 2022

#time.strfttime
# strftime 함수는 시간에 관계된 것을 세밀하게 표현하는 여러가지 포맷코드를 제공한다.
lastTime = time.strftime('%b',time.localtime(time.time()))
print(lastTime)

# 포맷코드	설명
# %a	요일(줄임)	→ Mon
# %A	요일	        → Monday
# %b	달(줄임)     → Jan
# %B	달	        → January
# %c	날짜와 시간을 출력함	→ 06/01/01 17:22:21
# %d	날(day)	    →[01,31]
# %H	시간(hour)-24시간 출력 형태 → [00,23]
# %I	시간(hour)-12시간 출력 형태 →   [01,12]
# %j	1년 중 누적 날짜  →	[001,366]
# %m	달   →	[01,12]
# %M	분   →	[01,59]
# %p	AM or PM	→   AM
# %S	초	→   [00,59]
# %U	1년 중 누적 주-일요일을 시작으로	→   [00,53]
# %w	숫자로 된 요일	→   [0(일요일),6]
# %W	1년 중 누적 주-월요일을 시작으로	→   [00,53]
# %x	현재 설정된 로케일에 기반한 날짜 출력   →	06/01/01
# %X	현재 설정된 로케일에 기반한 시간 출력	  → 17:22:21
# %Y	년도 출력	→   2001
# %Z	시간대 출력	→   대한민국 표준시
# %%	문자	→   %
# %y	세기부분을 제외한 년도 출력	→   01

#time.sleep
# time.sleep함수는 주로 루프 안에서 많이 사용한다. 이 함수는 일정한 시간 간격을 두고 루프를 실행한다.
#sleep1.py
import time
for i in range(3):
    print(i)
    time.sleep(1)
#>>> 1초 단위로 0~9까지의 숫자를 출력한다.

#math.gcd
# math.gcd함수를 이용하면 최대공약수를 쉽게 구할 수 있다.(python 3.5버전이상부터)
import math
a = math.gcd(60,100,80)
print(a)
