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

a = SafeFourCal(4,0)
print(a.div())