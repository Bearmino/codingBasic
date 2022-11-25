#생성자(constructor)
# 객체가 생성될 때 자동으로 호출되는 메서드이다.

class FourCal:
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

a=FourCal()
#a.add()
# AttributeError:'FourCal' object has no arttribute 'first'오류가 발생한다."""
#
# FourCal()클래스의 인스턴스 a에 setdata메서드를 수행하지 않고 add메서드 실행시 위의 에러가 발생한다
# setdata메서드를 수행해야 객체 a의 객체변수 first와 second가 생성되기 때문이다.
#
# 하지만, 이렇게 객체의 초기값을 설정시에는 setdata와 같은 메서드 호출보다 "생성자"를 사용하는 것이 더 안전하다.
#

class FourCal1 :
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

b=FourCal1(4,2)
print(b.first,b.second)
print(b.add())

# __init__인 생성자 메서드를 사용시에는 setdata와는 다르게 생성자의 매개변수를
# class 선언 후 바로 전달 되어야 한다.

class Text :
    def __init__(self,name,text):
        self.name = name
        self.text = text
    def babo(self):
        print("%s는 %s입니다." % (self.name,self.text) )
    def sarang(self):
        print("%s는 나의 %s입니다."% (self.name,self.text))

a=Text("홍재","바보")
b=Text("승주","사랑")

a.babo()
b.sarang()
