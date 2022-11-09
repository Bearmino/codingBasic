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
print(a) # return이 아니다.
'''print문은 출력을 담당하는 요소 중 하나에 해당될 뿐 결과값은 아니다.'''
'''return 명령어만이 결과값으로 될 수 있다.'''

#입력값도 결과값도 없는 함수
def say():
    print('Hi')
say()
'''인수를 받는 매개변수도 없고, return값도 존재하지 않기에 입력값도 결과값도 존재하지 않느다.'''
'''해당 함수의 출력 방법은 함수이름으로밖에 없다.'''

#매개변수 지정하여 호출하기
def add(a,b):
    return a+b

result=add(a=3,b=7)
print(result)

result=add(a=5,b=8)
print(result)
"""매개변수를 지정하면 순서와 상관없이 사용이 가능하다는 장점이 있다."""

#여러 개의 입력값을 받는 함수 만들기
"""
def 함수(*매개변수):
    <수행할 문장>
"""
def add_money(*args):
    result=0
    for i in args:
        result = result + i
    return result
"""args는 임의로 정한 변수이름이다. 아무 이름이나 써도 된다."""
result = add_money(1,2,3,4,5)
print(result)

result = add_money(1,2,3,4,5,6,7,8,9,10)
print(result)

"""여러개의 입력 처리 시 매개변수로만 사용할 수 있는 것은 아니다."""
def add_mul(choice,*args):
    if choice =="add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result

result=add_mul('add',1,2,3,4,5)
print(result)

result=add_mul('mul',10,20,30,40,50)
print(result)
'''매개변수 choice에 'add'가 입력된 경우, *args에 입력되는 모든 값을 더해주고,'mul'이 입력된 경우 elif의 *args의 모든 값을 곱한다.'''