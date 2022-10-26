#딕셔너리(또는 해시(hash))란
'''
딕셔너리는 Key와 Value를 한쌍으로 갖는 자료형
ex) Key가 basebalss이라면 Value는 야구가 될 것이다.
'''

#딕셔너리의 예
dic ={'name':'peny','phone':'0110525424','birth':'1118'}
print(dic)

integer = {1:'hi'}
print(integer)

valueList = {'a':[1,2,3]}
print(valueList)

#딕셔너리 쌍 추가하기
a={1:'a'}
a[2]='b'
print(a)

a['name']='peny'
print(a)

a[3]=[1,2,3]
print(a)

#딕셔너리 요소 삭제하기
del a[1]
print(a)
'''a[key]에 해당하는 {key:value}값이 쌍으로 삭제됨'''

#딕셔너리의 key 사용으로 Value값을 얻기
grade = {'peny':10,'donut':20,'mali':30}
print(grade['peny'])
print(grade['donut'])

#딕셔너리 만들 때 주의사항
a={1:'a',1:'b'}
print(a)
