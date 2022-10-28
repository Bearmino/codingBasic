#변수란, 자료형의 값을 저장하는 공간

a=1
b="python"
c=[1,2,3]
'''위처럼 변수를 생성할때에는 =(assignment) 기호를 사용한다.'''
'''파이썬에서 변수는 객체를 가리키는 것으로 '객체'란 자료형과 같은 의미를 말한다. '''

a=[1,2,3]
print(id(a))
'''id함수는 변수가 가르키고 있는 객체의 주소값을 나타내는 내장함수이다. '''

print()

#리스트를 복사하고자 할때 함수
'''[:]를 이용'''
a=[4,5,6]
b=a[:]
print(a)
print(b)

'''copy모듈 이용'''
from copy import copy
a=[7,8,9]
b=copy(a)
print(a)
print(b)

#하기처럼 리스트를 이용한 복사 시 주의사항
a=[1,2,3]
b=a
print(b)
a[1]=4
print(a)
print(b)
print(id(a))
print(id(b))
'''위의 결과를 보면 id(a)의 값이 id(b)의 값과 동일함을 확인할 수 있다. 
그렇기에, a 리스트의 값을 변경하면 b의 리스트도 같이 변경된다.
이 점은 리스트 복사를 사용시에 주의해야 할 점이다.'''
print(a is b)
'''is 내장함수를 통해서도 같은 객체인지를 확인할 수 있다.'''

#변수를 만드는 여러가지 방법

a,b =('phthon','life')
print(a,b)

(a,b)='phthon','life'
print(a,b)

a=b='phthon'
print(a,b)

#두 변수를 바꾸는 방법

a=3
b=5
a,b=b,a
print(a,b)