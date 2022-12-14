#파이썬 내장함수
# 파이썬 내장 함수는 파이썬 모듈과 달리 import가 필요하지 않다.

#abs()
# abs(x),어떤 숫자를 입력 받았을 때, 그 숫자의 절대값을 리턴하는 함수
a=abs(-3)
print(a)
#>>>3

#all()
# 반복 가능한(iterable) 데이터 x를 입력 값으로 받으며, 이 x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False를 리턴
#반복 가능한 데이터란, for문에서 사용 가능한 자료형을 의미한다.(리스트, 튜플, 문자열, 딕셔너리, 집합등)

print(all([1,2,3]))
#>>>True

#리스트 중 0은 거짓이므로 False를 출력한다.
print(all([1,2,3,0]))
#>>>False

#all의 입력 인수가 빈 값인 경우에는 True를 리턴한다.
print(all([]))
#>>>True

#any
# 반복 가능한(iterable) 데이터 x를 입력으로 받아 x의 요소 중 하나라도 참이 있으면 True를 리턴하고, x가 모두 거짓일 때에만 False를 리턴한다
# all()의 반대이다.

#리스트 [1,2,3,0]중 1,2,3이 참이므로 True를 리턴
print(any([1,2,3,0]))
#>>>True

#리스트 [0,""]의 요소 0과 ""은 모두 거짓이므로 False를 리턴한다.
print(any([0,""]))
#>>>False

#any가 입력 인수가 빈 값의 경우 False를 출력한다.
print(any([]))
#>>>False

#chr
# 유니코드 숫자값을 입력받아 그 코드에 해당하는 문자를 리턴하는 함수
# 유니코드는 전세계의 모든 문자를 컴퓨터에서 일괄되게 표현하고 다룰 수 있는 설계된 산업 표준이다.
print(chr(97))
#>>>'a'
print(chr(44032))
#>>>'가'

#dir
# 객체가 지닌 변수나 함수를 보여 주는 함수이다.
print(dir([1,2,3]))
#>>>['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__'등 출력
print(dir({'1':'a'}))
#>>>['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__'등 출력

#divmod
# 2개의 숫자를 입력으로 받은 후, a를 b로 나눈 몫과 나머지를 튜플로 리턴하는 함수다.
print(divmod(7,3))
#>>>2,1 (2는 몫이고 1은 나머지다)

#enumerate
# '열거하다'라는 뜻으로, 이 함수는 순서가 있는 데이터(리스트,튜플,문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴한다.
# 보통 enumerate함수는 다음 예제처럼 for문과 함께 사용한다.
for i, name in enumerate(['body','foo','bar']):
    print(i,name)
#>>> 0 body
#>>> 1 foo
#>>> 2 bar

# 순서값과 함께 body,foo,bar가 순서대로 출력되어, 자료형의 현재 순서(index)와 그 값을 쉽게 알 수 있다.

#eval
# 문자열로 구성된 표현식을 입력으로 받아 해당 문자열을 실행한 결과값을 리턴하는 함수이다.
print(eval('1+2'))
#>>>3
print(eval("'hi'+'a'"))
#>>hia
print(eval('divmod(4,3)'))
#>>>(1,1)

#filter
# filter란 무엇인가를 걸러낸다는 뜻으로 첫번째 인수로 함수를, 두번째 인수로 그 함수에 차례로 들어갈 반복 가능한 데이터를 받는다.
# 반복 가능한 데이터(iterable)의 요소 순서대로 함수(func)를 호출 했을때 반환값이 참인것만 묶어서 리턴한다.

#positive.py
def positive(l):
    result=[]
    for i in l:
        if i>0:
            result.append(i)
    return result

print(positive([1,-3,2,0,-5,6]))
#>>>[1,2,6]
# 위의 positive함수는 리스트를 입력 받아서 각각의 요소를 판단하여 양수 값만 출력하는 함수이다.
# filter함수를 사용하여 위 내용과 같이 간단하게 작성이 가능하다.

#filter.py
def positive(x):
    return x>0

print(list(filter(positive, [1,-3,2,0,-5,6])))
#>>>[1,2,6]

#lambda식을 사용하게 되면,
print(list(filter(lambda x:x>0,[1,-3,2,0,-5,6])))
#>>>[1,2,6]

#hex
# 정수를 입력 받아 16진수(hexadecimal)문자열로 리턴하는 함수이다.
print(hex(234))
#>>>0xea
print(hex(3))
#>>>0x3

#id
# id(object)는 객체를 입력받아 객체의 고유 주소 값(레퍼런스)을 리턴하는 함수이다.
a=3
print(id(3))
#>>2930422238296
print(id(a))
#>>2930422238296
b=a
print(id(b))
#>>2930422238296

#3,a,b 세개가 모두 동일한 주소값을 가지고 있다.

#input
# input([prompt])는 사용자 입력을 받는 함수이다. 입력 인수로 문자열로 처리된다.
a=input("Enter: ")
print(a)

#int
# 문자열 형태의 숫자나 소수점이 있는 숫자를 정수로 리턴하는 함수이다.(정수는 그대로 리턴)
print(int('3'))
#>>>3
print(int(3.4))
#>>>3
#int(x,radix)는 radix 진수로 표현된 문자열 X를 10진수로 변환하여 리턴한다.
print(int('11',2))
#>>>3
#16진수로 표현된 1A의 10진수 값도 리턴 가능하다.
print(int('1A',16))
#>>>26

#inistance
# 첫번째 인수로 객체, 두번째 인수로 클래스를 받는다.
# 입력받은 객체가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 리턴한다.
class Person:pass

a=Person()
out=isinstance(a,Person)
print(out)
#>>>True
#a객체가 Person클래스에 의해 생성된 인스턴스임을 확인할 수있다.

b=3
out=isinstance(b,Person)
print(out)
#>>>False
#b는 Person()클래스가 아니므로 False를 출력한다.

#len
# 입력값 s의 길이(요소의 전체 개수)를 리턴하는 함수이다.
print(len("Python"))
#>>> 6
print(len([1,2,3]))
#>>> 3
print(len((1,'a')))
#>>> 2


#list
# 반복(iterable)는 반복 가능한 데이터(iterable)를 입력 받아 리스트로 만들어 리턴하는 함수이다.
print(list("pyhthon"))
#>>>['p', 'y', 'h', 't', 'h', 'o', 'n']
print(list((1,2,3)))
#>>>['1','2','3']

#map
# map(f,iterable)은 함수(f)와 반복 가능한 데이터를 입력으로 받는다.
# map함수는 입력받은 데이터의 각 요소에 함수 f를 적용한 결과를 리턴하는 함수다.

#two_times.py
def two_times(numberList):
    result=[]
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1,2,3,4])
print(result)
#>>>[2,4,6,8]

#two_times함수는 리스트를 입력 받아 리스트이 각 요소에 2를 곱해 리턴하는 함수다.
#map 함수를 사용하여 다음처럼 변경할 수 있다.
def two_times(x):
    return x*2

out=list(map(two_times,[1,2,3,4]))
print(out)
#>>>[2,4,6,8]

# map함수의 결과를 출력하기 위해 list를 사용함(map함수는 map 객체를 리턴한다.)
# lambda를 사용하면,

out=list(map(lambda x:x*2,[1,2,3,4]))
print(out)
#>>>[2,4,6,8]

#max
# max(iterable)함수는 인수로 반복 가능한 데이터를 입력받아 그 최대값을 리턴한다.
a=[1,2,3]
out = max(a)
print(out)
#>>> 3

#min
# max함수와는 반대로 그 최소값을 리턴한다.
a=[1,2,3]
out = min(a)
print(out)
#>>> 1

#oct
# oct(x)는 정수를 8진수 문자열로 바꾸어 리턴하는 함수이다.
print(oct(34))
#>>>0o42
print(oct(12345))
#>>>0o30071

#open
# open(filename,[mode])은 "파일이름"과 "읽기방법"을 입력 받아 파일 객체를 리턴하는 함수다.
# 읽기 방법(mode)를 생략하면, 기본값일 읽기모드(r)로 객체를 만들어 리턴한다.
# mode | 종류
# w | 쓰기 모드로 파일 열기
# r | 읽기 모드로 파일 열기
# a | 추가 모드로 파일 열기
# b | 바이너리 모드로 파일 열기
#b는 w,r,a와 함께 사용한다.

#ord
# ord(c)는 문자의 유니코드 숫자 값을 리턴하는 함수다.
# ord는 chr함수와 반대이다.
print(ord('a'))
#>>>97
print(ord('가'))
#>>>44032

#pow
# pow(x,y)는 x의 y 제곱한 결과값을 리턴하는 함수다.
print(pow(2,4))
#>>>16
print(pow(3,3))
#>>>27

#range
# range([start,]stop[,step])는 for문과 함께 자주 사용하는 함수이다.
# 이 함수는 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 리턴한다.

#인수가 하나인 경우
print(list(range(5)))
#>>>[0, 1, 2, 3, 4]
#시작 숫자를 정하지 않으면 range는 0부터 시작한다.

#인수가 2개인 경우
print(list(range(5,10)))
#>>>[5, 6, 7, 8, 9]
#입력으로 주어진 숫자의 시작과 끝숫자를 나타낸다. 단 끝 숫자는 해당 범위에 포함되지 않는다.

#인수가 3개인 경우
print(list(range(1,10,2)))
#[1, 3, 5, 7, 9]
#세번째 숫자는 숫자 사이의 거리를 말한다.

#round
# round(number[,ndigits])함수는 숫자를 입력받아 반올림해 리턴하는 함수이다.
print(round(4.6))
#>>> 5
print(round(5.472,2))
#>>> 5.47
#round함수의 두번째 인수는 반올림하여 표시하고 싶은 소숫점 자리수이다.

#sorted
# sorted(iterable)함수는 입력 데이터를 정렬한 후 그 결과를 리스트로 리턴하는 함수이다.
print(sorted([3,1,2]))
#>>>[1,2,3]
print(sorted(['a','c','b']))
#>>>[a,b,c]
print(sorted((3,2,1)))
#>>>[1,2,3]
print(sorted("zero"))
#>>>['e','o','r','z']
#리스트 자료형에도 sort함수가 있다. 하지만, 리스트 자료형의 sort함수는 리스트 객체 그 자체를 정렬만 할 뿐 결과를 리턴하지 않는다.

#str
# str(object)은 문자열 형태로 객체를 변환하여 리턴하는 함수이다.
print(str(3))
#>>>'3'
print(str('hi'))
#>>>'hi'

#sum
# sum(iterable)함수는 입력 데이터의 합을 리턴하는 함수이다.
print(sum([1,2,3]))
#>>> 6
print(sum((4,5,6)))
#>>> 15

#tuple
# tuple(iterable)은 반복 가능한 데이터를 튜플로 바꾸어 리턴하는 함수이다.
# 만약 입력이 튜플인 경우에는 그대로 리턴한다.
print(tuple("abc"))
#>>>('a', 'b', 'c')
print(tuple([1,2,3]))
#>>>(1,2,3)
print(tuple((1,2,3)))
#>>>(1,2,3)

#type
# type(object)은 입력값의 자료형이 무엇인지 알려주는 함수이다.
print(type("abc"))
#>>><class 'str'>
print(type([ ]))
#>>><class 'list'>
print(open("test",'w'))
#>>><class 'io.TextIOWrapper'>

#zip
# zip(*iterable)은 동일한 개수로 이루어진 데이터들을 묶어서 리턴하는 함수이다.
print(list(zip([1,2,3],[4,5,6])))
#>>>[(1, 4), (2, 5), (3, 6)]
print(list(zip([1,2,3],[4,5,6],[7,8,9])))
#>>>[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
print(list(zip("abc","def")))
#>>>[('a', 'd'), ('b', 'e'), ('c', 'f')]

