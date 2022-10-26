odd = [1,3,5,7,9]
print(odd)

#리스트는 생김새에 따라 다음과 같음
a=[] #a=list()로 빈열을 생성할 수 있다.
b=[1,2,3]
c=['Life','is','too','short']
d=[1,2,'Life','is']
e=[1,2,['Life','is']]
print(a,b,c,d,e)

#리스트 값의 사칙연산
f=[1,2,3,4]
print(f[0]+f[2])
print(f[2]*f[3])
print(f[-1]) #-1의 요솟값은 리스트의 맨 마지막을 말한다.

#다중 리스트 인덱싱 및 위치 반화(index)
a=[0,[1,2,3]]
print(a[-1][0])
b=[1,2,3]
b.index(2)
print(b)

#리스트 슬라이싱
a=[1,2,3,4,5]
print(a[0:2])
b="1,2,3,4,5"
print(b[0:3])

#리스트 더하기,반복하기
a=[1,2,3]
b=[3,4,5]
print(a+b)

a=[1,2,3]
print(a*3)

#리스트 길이 구하기
a=[1,2,3,4,5,6]
print(len(a))

#리스트에서 값 수정
a=[1,2,3]
a[2]=4
print(a[2])

#리스트에서 값 삭제 및 요소 지우기
a=[1,2,3]
del a[1]
print(a)
b=[1,2,3,4,5]
b.remove(3)
print(b)

b=[1,2,3,4,5]
del b[3:]
print(b)

#리스트 요소 추가(append)
a=[1,2,3]
a.append(4)
print(a)

#리스트 정렬(sort) 및 뒤집기(reverse)
a=[1,4,3,2,6]
a.sort()
print(a)
b=[2,4,1,6,5,3]
b.reverse()
print(b)

#리스트에서 선택 요소 끄집어내기
a=[1,2,3,4,5]
a.pop() #아무런 요건이 없을때는 맨 마지막을 제외한다.
print(a)
b=[1,2,3,4,5]
b.pop(0)
print(b)

#리스트에 포함된 요소 x의 개수 세기(count)
a=[1,2,1,4,1,6,7]
print(a.count(1))

#리스트 확장(extend)
a=[1,2,3]
a.extend([4,5,6])
print(a)