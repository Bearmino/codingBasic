#불(bool) 자료형이란 참(true)과 거짓(false)을 나타내기 위한 자료형이다.
'''True,False는 예약어로 앞에는 대문자로 시작'''
a=True
b=False

print(type(a))
print(type(b))
'''type(x)는 x의 자료형을 확인하는 파이썬의 내장 함수'''

print(1==1)
print(2>1)
print(1>2)
'''불 자료형은 조건문의 반환 값으로도 사용된다.'''
'''문자열,리스트,튜플,딕셔너리등의 값이 비어 있으면 거짓으로 된다.'''

print(bool(''))
print(bool([]))
print(bool(0))

if[]:
    print("참")
else:
    print("거짓")




