"""앞서 익힌 함수를 이용해서 계산기의 "더하기"기능의 파이썬 코드 구현"""
result=0

def add(num):
    global result #이전 결과값을 유지하기 위한 전역변수 (global)을 사용함
    result+=num
    return result

print(add(3))
print(add(5))

# 만일 계산기가 2개가 필요하다면..

result1 = 0
result2 = 0

def add(num):
    global result1
    result1+=num
    return result1
def add(num):
    global result2
    result2+=num
    return result2

print(add(3))
print(add(4))
print(add(5))
print(add(6))

# Class를 활용한 메소드 활용
class Calculator:
    def __init__(self):
        self.result=0

    def add(self,num):
        self.result+=num
        return self.result

cal1=Calculator() #cal1의 객체생성
cal2=Calculator() #cal2의 객체생성

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

#클래스와 객체
"""   """