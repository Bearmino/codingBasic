# 앞서 익힌 함수를 이용해서 계산기의 "더하기"기능의 파이썬 코드 구현
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
# 과자를 만든다고 생각을 해보자.
# 과자 틀 → 클래스(Class)
# 과자틀에 의해 만든 과자 → 객체(Object)
#
# 즉, 클래스(class)란 똑같은 무엇인가를 계속해서 만들어 낼 수 있는 설계도면과 같고,
# 객체(object)란 클래스로 만든 피조물을 뜻한다.
#
# 클래스로 만든 객체들은 서로 영향을 주지 않는다.
#

class Cookie:
    pass #pass는 아무것도 수행하지 않는 문법으로 임시로 코드 작성시 사용
a= Cookie()
b= Cookie()
# 클래스로 만든 객체(a,b)를 cookie클래스의 인스턴스라고 한다.

#사칙연산 클래스 만들기

#   1. 클래스 구조 만들기
# class FourCal:
    # pass
# a=FourCal()
# print(type(a))
#   type을 통해서 객체 a가 FourCal클래스의 인스턴스임을 알 수 있다.

#   2. 객체에 숫자 지정 만들기
class FourCal:
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
# 파이썬 메서드의 첫 번째 매개변수 이름은 관례적으로 self를 사용한다.

a=FourCal()
a.setdata(4,2)
# etdata메서드의 첫번째 매개변수 self에는 setdata메서드를 호출한 객체 a가 자동으로 전달된다.

print(a.first,a.second)
# a → self , 4 → first, 2 → second, setdata 메서드의 매개변수 first,second에 4,2가 전달

b=FourCal()
b.setdata(3,7)
print(b.first)
# FourCal클래스의 인스턴스인 b라는 객체를 새롭게 생성 후 setdata를 이용하여 매개변수 3,7전달
print(b.first == a.first)
# 해당 수식을 이용하여 확인해 보면 a 객체의 first값과 b 객체의 first값에 영향을 받지 않는다.

# 더하기 기능 만들기
    # def add(self):
    #     result = self.first + self.second
    #     return result
# add 메서드의 매개변수는 self이고, 반환값은 result이다.!!
print(a.add())
# a.add()와 같이 a 객체에 의해 add메서드가 수행되면서 add메서드의 self에는 객체 a가 자동으로 입력됨
print(a.mul())
print(a.sub())
print(a.div())
print(a.mul())


