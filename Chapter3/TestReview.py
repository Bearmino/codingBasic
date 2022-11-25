
class Text :
    def sarang(self,name,text):
        print("%s님은 나의 %s입니다."% (name,text))
    def babo(self,name,text):
        a={'1':name,'2':text} # 딕셔너리를 활용함
        # print("%s는 %s입니다." % (self.name,self.text))
        print(f'{a["1"]}는 {a["2"]}입니다.')

a=Text()
b=Text()

a.sarang("동경","사랑")
b.babo("홍재","바보")