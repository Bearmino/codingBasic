# 오류는 어떤 때 발생하는가?
# 프로그램을 만들다 보면 수없이 많은 오류를 만나지만, 오류가 발생하는 이유는 프로그램이 잘못 동작되는 것을 막는 행위이기도 하다.
# 오타를 입력했을 때에 발생하는 구문 오류를 제외한 오류에 대해 살펴보자.

#[존재하지 않는 파일을 사용하려고 시도할때 발생하는 오류] : FileNotFoundError
# >>>f = open("나없는파일",'r')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# FileNotFoundError: [Errno 2] No such file or directory: '나없는파일'

#[0으로 다른 숫자를 나누는 경우에 발생하는 오류] : ZeroDivisionError
# 4/0
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero

#[리스트에서 얻을 수 없는 값을 요청하여 발생하는 오류] : IndexError
# >>> a = [1,2,3]
# >>> a[4]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range

#오류 예외 처리 기법
#try... except문(구조)
#try:
#   ...
#except[발생오류[as 오류변수]]:
#   ...

#try 블록 수행 주 오류가 발생 시 except블록을 수행한다.
#하지만 try블록에서 오류가 발생하지 않으면, except블록은 수행되지 않는다.

#1. [try,except만 쓰는 방법]
#try:
#   ...
#except:
#   ...
#>>>오류 종류에 상관없이 오류가 발생하면 except블록 수행

#2. [발생 오류만 포함하는 except문]
#try:
#   ...
#except 발생오류:
#   ...
#>>>오류 발생 시에 except문에 미리 정해 놓은 오류와 동일한 오류일 경우,,except블록을 수행 진행

#3. [발생 오류와 오류변수까지 포함한 except문]
#try:
#   ...
#except 발생오류 as 오류변수:
#   ...
#>>> 오류의 내용까지 알 수 싶은 경우 사용하는 방법

try:
    4/0
except ZeroDivisionError as e:
    print(e)

#try .. finally
# finally절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행된다.
# 보통 finally절은 사용한 리소스를 close해야 할 떄에 많이 사용한다.
#try: 
# f = open('foo.txt', 'w')
#   ....(무언가를 수행)
# finally:
#   f.close() <- 중간에 오류가 발생하더라도 무조건 실행한다.

# 여러개의 오류 처리하기
# try:
#   ....
# except 발생오류1:
#   ....
# except 발생오류2:
#   ....

try:
    a=[1,2,3]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로는 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")
#>>> a는 2개의 요소값을 가지기에 a[3]는 IndexError를 발생시키므로 "인덱싱 할 수 없습니다"라는 문구가 발생된다.
#인덱싱 오류가 먼저 발생하였기에, ZeroDivisionError는 발생되지 않는다.

try:
    a=[1,2]
    print(a[3])
    4/0
except (ZeroDivisionError,IndexError) as e:
    print(e)
# 2개 이상의 오류를 동일하게 처리하기 위해서 위와 같이 괄호로 묶어 처리하면 된다.

#try ... else
#try:
#   ...
#except [발생오류 [as  오류변수]]:
#   ...
#else:
#   ...
#>>> try문 수행 중 오류가 발생하면 except절이 수행되고 오류가 없으면 else절이 수행된다.
try:
    age=int(input("나이를 입력하세요 : "))
except:
    print("입력이 정확하지 않습니다.")
else:
    if age<=18:
        print("미셩년자입니다.")
    else:
        print("성인입니다.")
#>>> 숫자가 아닌 다른 값을 입력시에는 '입력이 정확하지 않습니다.'라는 문장을 출력한다.
#오류가 없을 시 else문을 실행

#오류 회피하기
# 코드를 작성 시 특정 오류가 발생할 경우, 그냥 통과시켜야 할 때 사용
try:
    f = open("나없는파일",'r')
except FileNotFoundError:
    pass

#오류 일부러 발생 시키기
# 프로그래밍을 하다 보면 종종 오류를 일부러 발생시켜야 할 경우도 생긴다.
# 파이썬의 경우 raise 명령어를 사용해 오류를 강제로 발생시킨다.

# Bird 클래스를 상속 받는 자식 클래스는 반드시 fly라는 함수를 구현하도록 만들고 싶은 경우
class Bird:
    def fly(self):
        raise NotImplementedError

# class Eagle(Bird):
#     pass
#
# eagle = Eagle()
# eagle.fly()
#>>> raise NotImplementedError
#>>> NotImplementedError
# Eagle클래스는 Bird 클래스를 상속 받았다. 그러나 Eagle클래스는 fly메서드를 오버라이딩하여 구현되지 않음
# 따라서, eagle객체의 fly메서드를 수행하는 순간 Bird클래스의 fly메서드가 수행되어 NotImplementedError가 발생

class Eagle(Bird):
    def fly(self):
        print("I'm fly")

eagle2 = Eagle()
eagle2.fly()
#NotImplementedError가 발생되지 않도록, 함수를 구현해줘야한다.(오버라이딩)

#예외 만들기
# 프로그램 수행 도중 특수한 경우에만, 예외 처리를 하기 위해서 종종 예외를 만들어 사용한다.
# 예외는 다음과 같이 python 내장 클래스인 Exception클래스를 상속하여 만들 수 있다.
class MyError(Exception):
    pass

def say_nick(nick):
    if nick=="바보":
        raise MyError()
    print(nick)

say_nick("천재")
#say_nick("바보")
# say_nick("바보")에서 MyError가 발생한다. 해당 부분을 예외처리 해보자.

try:
    say_nick("천재")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")

# 만약 오류 메시지를 사용하고 싶다면, 다음처럼 예외 처리를 해주면된다.

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 오류입니다."

def say_nick(nick):
    if nick=="바보":
        raise MyError()
    print(nick)

try:
    say_nick("천재")
    say_nick("바보")
except MyError as e:
    print(e)