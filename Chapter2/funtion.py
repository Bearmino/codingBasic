#함수(funtion)
"""1. 반복적으로 사용되는 가치 있는 부분을 뭉치로 묶어서 어떤 입력 값 주었을 때 어떤 결과값을 돌려준다."""
"""2. 자신이 만든 프로그램을 함수화하면 프로그램 흐름을 일목요연하게 볼 수 있다."""

#파이썬 함수의 구조
def add(a,b): #def 함수명(매개변수):
    return a+b #<수행할 문장1>
'''def는 예약어이며, 함수이름은 함수를 만드는 사람이 임의로 설정이 가능하다.'''
a=2
b=3
c=add(a,b)
print(c)
'''해석하면 이 함수의 이름(함수이름)은 add이고, 입력으로 2개의 값을 받으면 결과값은 2개의 입력을 더한값이다.'''

#매개변수와 인수
def add(a,b): #a,b는 매개변수
    return a+b
print(add(3,4)) #3,4는 인수

#일반적인 함수
def add(a,b):
    result = a+b
    return result

a=add(3,4)
print(a)

#입력값이 없는 함수
def say():
    return 'Hi'
print(say())

#결과값이 없는 함수
def add(a,b):
    print("%d,%d의 합은 %d입니다."% (a,b,a+b))
a=add(3,4)
print(a)
'''print문은 출력을 담당하는 요소 중 하나에 해당될 뿐 결과값은 아니다.'''
'''return 명령어만이 결과값으로 될 수 있다.'''


#입력값도 결과값도 없는 함수
def say():
    print('Hi')



