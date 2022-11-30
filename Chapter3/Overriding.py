#오버라이딩

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

#SafeFourCal클래스는 FourCal 클래스에 있는 div메서드를 동일한 이름으로 다시 작성
#부모클래스(상속한클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것을 메서드 오버라이딩이라 한다.
#메서드를 오버라이딩하면 부모클래스의 메서드 대신 오버라이딩 메서드가 호출된다.
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4,2)
print(a.div())

#클래스 변수
#객체변수는 다른 객체들의 영향을 받지 않고 독립적으로 그 값을 유지하지만 클래스 변수는 객체 변수와 성격이 다르다.
#클래스이름.클래스변수로 이용할 수 있다.

class Family:
    lastname = "박"

print(Family.lastname)
a=Family()
b=Family()

print(a.lastname)
print(b.lastname)
# 클래스 변수 값을 변경하면, 클래스로 만든 객체의 변수도 모두 동일하게 변경된다.
# 클래스 변수와 동일한 이름의 객체 변수를 생성하면??
a.lastname="최"
print(a.lastname)
print(b.lastname)
# 클래스의 변수가 바뀌는 것이 아닌 a객체에 lastname이라는 객체변수가 새롭게 생성된다.
# 객체변수는 클래스변수와 동일한 이름으로 생성할 수 있다.