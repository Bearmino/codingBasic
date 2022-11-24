# 상속(Inheritance)
# "물려받다"라는 의미로 어떤 클래스를 만들 때 다른 클래스의 기능을 물려 받을 수 있다.

class FourCal:
    def __init__(self,first,second):
        self.first = first
        self.second = second

    def add(self):
        result=self.first+self.second
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

#class클래스 이름(상속할 클래스 이름)
class MoreFourCal(FourCal):
    pass

#MoreFourCal에서 FourCal클래스의 기능을 모두 사용할 수 있다.
a=MoreFourCal(4,2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

#상속을 하는 이유
#클래스의 기능을 추가하고 싶으면 기존 클래스를 수정하면 되지만, 기존 클래스가 라이브러리 형태로 제공되거나
#수정이 허용되지 않는 상황이라면 상속을 사용해야 한다.

#a의 n제곱(aⁿ)을 계산하는 MoreFourCal클래스를 만들어보자.
class MoreFourCal(FourCal):
    def pow(self):
        result=self.first ** self.second
        return result

b=MoreFourCal(5,2)
print(b.pow())










