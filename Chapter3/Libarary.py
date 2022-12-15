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
result = math.gcd(60,100,80)
print(result)

#math.lcm
# math.lcm은 최소공배수를 구할때 사용하는 함수
import math
result = math.lcm(20,30)
print(result)

#random
# random은 난수(규칙이 없는 임의의 수)를 발생시키는 모듈이다.
import random
print(random.random())
#0.0~1.0사이에서의 난수 값 구하기
print(random.randint(1,10))
#1~10사이에서의 난수 값 구하기

#itertools.zip_longest
# 같은 개수의 자료형을 묶는 파이썬 내장 함수인 zip()과 동일한 동작한다.
# 하지만, 전달한 반복 가능 객체의 길이가 다르다면 긴 것을 기준으로 빠진 값은 fillvalue에 설정한 값으로 채울 수 있다.
# 별도의 채우는게 없다면 None을 출력한다.
import itertools

students = ['한민관','황지민','이영희','이영철','오민식']
snacks = ['사탕','초콜릿','젤리','새우깡']

result = itertools.zip_longest(students,snacks,fillvalue='초코파이')
print(list(result))
#>>> [('한민관', '사탕'), ('황지민', '초콜릿'), ('이영희', '젤리'), ('이영철', '새우깡'), ('오민식', '초코파이')]

#itertools.permutation
# 반복 가능 객체(iterable)중에서 r개를 선택한 순열을 이터레이터로 리턴하는 함수이다.
import itertools
for a,b in itertools.permutations(['1','2','3'],2):
    print(a+b)
#>>>12
#   13
#   21
#   23
#   31
#   32

#functool.reduce
# function을 반복 가능한 객체(iterable)의 요소에 차례대로(왼쪽 → 오른쪽)누적 적용하여 객체를 하느이 값으로 줄이는 함수
def add(data):
    result = 0
    for i in data:
        result+=i
    return result

data = [1,2,3,4,5]
result = add(data)
print(result)
#>>>15

import functools
data = [1,2,3,4,5,6]
result = functools.reduce(lambda x,y: x+y,data)
print(result)
#>>>21
#((((1+2)+3)+4)+5) 람다식 적용방식

num_list=[3,15,2,20,40,7]
max_num = functools.reduce(lambda x,y: x if x>y else y, num_list)
print(max_num)

#operator.itemgetter
# sorted와 같은 함수의 key 매개변수에 적용하여 다양한 기준으로 정렬할 수 있도록 도와주는 모듈이다.
from operator import itemgetter
students = [
    ("jane",22,'A'),
    ("dave",32,'B'),
    ("sally",17,'C'),
]
result = sorted(students,key=itemgetter(1))
print(result)
#>>>[('sally', 17, 'C'), ('jane', 22, 'A'), ('dave', 32, 'B')]
#itemgetter(1)은 students(튜플)의 2번째 요소를 기준으로 정렬하겠다는 의미이다.

students = [
    {"name":"jane","age":22,"grade":'A'},
    {"name": "dave", "age": 32,"grade": 'B'},
    {"name": "sally", "age": 17,"grade": 'C'},
]

result = sorted(students,key=itemgetter("age"))
print(result)
#>>>[{'name': 'sally', 'age': 17, 'grade': 'C'}, {'name': 'jane', 'age': 22, 'grade': 'A'},
# {'name': 'dave', 'age': 32, 'grade': 'B'}]
#딕셔너리 키인 age를 기준으로 정렬을 진행함

#operator.attrgetter()
#Student 클래스의 객체라면 다음처럼 attrgetter()를 적용해 정렬해야한다.
from operator import attrgetter
class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

students = [
    Student('Jane',22,'A'),
    Student('Dany',15,'B'),
    Student('Wendy',30,'C'),
]
result = sorted(students, key=attrgetter('age'))
print(result)


#shutil
# shutil은 파일을 복사(copy)하거나 이동(move)할 때 사용하는 모듈
# c:\doit이라는 폴더의 a.txt파일을 a.txt.bak이라는 파일로 복사하는 프로그램을 만들고자 한다면 아래처럼 해주면 된다.
# import shutil
# shutil.copy("c:/doit/a.txt","c:/doit/a.txt.bak")
# shutil.move("c:/doit/a.txt","c:/doit/game/a.txt")

#glob
# 파일을 읽고 쓰는 기능이 있는 프로그램을 만들다 보면 특정 디렉터리에 있는 파일 이름을 모두 알아야 할 때가 있을 경우 사용하는 모듈
import glob
print(glob.glob("c:/doit/foo*"))
#>>>'c:/doit\\foo.txt', 'c:/doit\\foo2.txt']

#pickle
# 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
# pickle 모듈의 dump함수를 사용하여 딕셔너리 객체인 data를 그대로 파일에 저장
import pickle
f = open("test.txt",'wb')
data = {1:'python',2:'you need'}
pickle.dump(data,f)
f.close()
# pickle.dump로 저장한 파일을 pckle.load를 사용해서 원래 있던 딕셔너리 객체(data)상태 그대로 불어오는 상황
import pickle
f = open("test.txt",'rb')
data = pickle.load(f)
print(data)

#os
# 환경 변수나 디렉터리,파일 등의 os자원을 제어할 수 있도록 해주는 모듈
#내시스템의 환경 변수값을 알고 싶을 때
import os
result = os.environ
print(result)
#>>> environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\Cloudike\\AppData\\Roaming',
# 'CLASSPATH': '%JAVA_HOME%\\lib;.....


