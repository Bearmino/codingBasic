#모듈
#함수나 변수 또는 클래스를 모아 놓은 파이썬 파일이다.
#또한, 모듈은 다른 파이썬 프로그램을 불러와 사용할 수 있게끔 만든 파이썬 파일이다.

#모듈 만들기
#mod1.py
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

print(add(4,2))
print(sub(5,2))

#해당 모듈을 c:\doit이라는 폴더를 만든 후 해당 위치로 저장
#윈도우 프롬프트를 통해서, 작성한 mod1.py파일에 대해 실행하여 본다.
#1. cd c:\doit으로 해당 폴더로 이동
#2. dir명령어를 통해서 디렉토리 목록 확인
#3. python을 입력하여 실행한다.(하기의 좀 더 다양한 실행방식 지정)
#4. import mod1를 입력하여 모드를 불러온 후 (import 모듈이름)
#5. print(mod1.add(숫자,숫자))명령어를 통해서 실행이 되는 확인
# "."(토트연산자)를 통해서 함수를 불러온다.

#다양한 실행 방식
#from 모듈 import 모듈함수
# >>> from mod1 import add
# >>> add(3,4)
# 7


#from 모듈 import 모듈함수1, 모듈함수2
# >>> from mod1 import add, sub
# >>> add(3,4)
# 7
# >>> sub(5,2)
# 3

#from 모듈 import *
# >>> from mod1 import * (mod1의 모든함수 사용)

#if_name_=="_main_":의 의미
# 다양한 함수들을 담고 있는 특정 파일이 import되어 함수도 제공해주지만 파일 그 자체가 실행도 되어 사용되어야 할때 사용함



