#함수(funtion)
# 1. 반복적으로 사용되는 가치 있는 부분을 뭉치로 묶어서 어떤 입력 값 주었을 때 어떤 결과값을 돌려준다.
# 2. 자신이 만든 프로그램을 함수화하면 프로그램 흐름을 일목요연하게 볼 수 있다.

#파이썬 함수의 구조
def add(a,b): #def 함수명(매개변수):
    return a+b #<수행할 문장1>
# def는 예약어이며, 함수이름은 함수를 만드는 사람이 임의로 설정이 가능하다.
a=2
b=3
c=add(a,b)
print(c)
# 해석하면 이 함수의 이름(함수이름)은 add이고, 입력으로 2개의 값을 받으면 결과값은 2개의 입력을 더한값이다.

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
# print문은 출력을 담당하는 요소 중 하나에 해당될 뿐 결과값은 아니다.
# return 명령어만이 결과값으s로 될 수 있다.

#입력값도 결과값도 없는 함수
def say():
    print('Hi')
say()
# 인수를 받는 매개변수도 없고, return값도 존재하지 않기에 입력값도 결과값도 존재하지 않느다.
# 해당 함수의 출력 방법은 함수이름으로밖에 없다.

#매개변수 지정하여 호출하기
def add(a,b):
    return a+b

result=add(a=3,b=7)
print(result)

result=add(a=5,b=8)
print(result)
# """매개변수를 지정하면 순서와 상관없이 사용이 가능하다는 장점이 있다."""

#여러 개의 입력값을 받는 함수 만들기
# ------------------------------------
# def 함수(*매개변수):
#     <수행할 문장>
# ------------------------------------
def add_money(*args):
    result=0
    for i in args:
        result = result + i
    return result
# args는 임의로 정한 변수이름이다. 아무 이름이나 써도 된다.
result = add_money(1,2,3,4,5)
print(result)

result = add_money(1,2,3,4,5,6,7,8,9,10)
print(result)

# 여러개의 입력 처리 시 매개변수로만 사용할 수 있는 것은 아니다.
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
# 매개변수 choice에 'add'가 입력된 경우, *args에 입력되는 모든 값을 더해주고,'mul'이
# 입력된 경우 elif의 *args의 모든 값을 곱한다.

#키워드 파라미터 kwargs
# 키워드 파라미터를 사용시에는 매개변수 앞에 별 두개(**)를 붙인다.

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
# {'a':1}'
print_kwargs(name='foo',age=3)
# {'name':'foo','age':3}
# 입력한 값들이 모두 딕셔너리로 만들어져서 출력된다는 것을 확인할 수 있다.
# 매개변수 앞에 **을 붙이면 매개변수 kargs는 모든 딕셔너리가 되고 모든 key=value형태의 결과값 출력한다.
# kwargs는 keyword arguments의 약자로, args와 마찬가지로 관례적으로 사용한다.

#함수의 결과값은 언제나 하나다.
def add_and_mul(a,b):
    return a+b,a*b

result = add_and_mul(3,4)
print(result)
# add_and_mul함수의 결과값은 a+b와 a*b로 튜플값이 하나인 (a+b,a*b)로 돌려준다.

result1, result2 = add_and_mul(3,4)
print("result1 =",result1,"result2=",result2)

# return의 다른 쓰임새
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s 입니다"% nick)

say_nick("멍충이")
say_nick("바보")
# 위에서 보면 say_nick이라는 함수를 지정하였으며, 반환값은 없다. 그렇기에, 만약에 입력값이 '바보'라는 값이
# 들어오면 문자열을 출력하지 않고 함수를 즉시 빠져 나간다.

#매개변수에 초기값을 미리 설정하기
# 다른 형태로 함수의 인수를 전달하는 방법
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다"% name)
    print("나이는 %d살 입니다."% old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

print(say_myself("신동석",40,True))
print(say_myself("오민식",39,False))
# 위 함수를 보면 매개변수가 name, old, man=True 3개이다. 그 중 man=True처럼 매개변수에
# 미리 값을 넣어 주어서 매개변수 초기값을 설정할 수 있다.
# 출력값을 보면 Flase에서는 여자입니다라고 출력이 된다.
# (중요!) 초기화 시킬 매개변수는 항상 맨 뒤로 놓아야 한다.

#함수 안에서 선언한 변수의 효력 범위
a=1
def vartest(a):
    a=a+1
vartest(a)
print(a)
# vartest함수에서 매개변수 a의 값에 1을 더했으니까 2가 출력될거 같지만, 결과값은 1이 나온다.
# 이처럼 나온 이유는 함수 안에서 새로 만든 매개변수는 함수안에서만 사용하는 "함수만의 변수"이다.

def vartest(z):
    z=z+1
vartest(3)
# print(z) 에러발생 '''
# 에러가 발생하는 이유는 vartest(3)을 수행하면 해당 함수에서의 값이 4가 나오지만
# 함수 호출이 끝난뒤의 print(z)의 경우에는 z라는 변수를 찾을 수가 없기에 에러 발생

#함수 안에서 함수 밖의 변수를 변경하는 방법

# 1. return 사용하기
a=1
def vartest(a):
    a=a+1
    return a
a=vartest(a)
print(a)
# return을 활용하여 vartest함수의 입력으로 들어온 값의 1을 더한값을 돌려준다.
# 따라서 a=vartest(a)라고 하면 vartest(a)의 바뀐 결과값이 들어온다.
#
# 2. global 명령어 사용하기
a=1
def vartest():
    global a
    a=a+1
vartest()
print(a)
# global 명령어를 사용하여서 global a문장은 함수 안에서 함수 밖의 a변수를 직접 사용하겠다는 뜻이다.

#lambda
# lambda(람다)는 함수를 생성할 때 사용하는 예야어로 def와 동일한 역활을 한다.
# 보통 함수를 한줄로 간결하게 만들 때 사용한다.

add = lambda a,b: a+b
result=add(3,4)
print(result)

# lambda 예약어로 만든 함수는 return 명령어가 없어도 결과값을 돌려준다.