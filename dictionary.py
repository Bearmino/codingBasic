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
a={1:'a',1:'b',1:'c'}
print(a)
'''이렇게 key값이 중복될 경우에는 어떤 key값을 불러와야는지 알 수 없기에, 최종(key:value)값을 제외한 값은 무시한다 '''

#딕셔너리 관련 함수
a={'name':'peny','phone':'011052547','birth':'1125'}
print(a.keys())
'''a.keys()는 딕셔너리 a의 key만을 모아서 dict_keys라는 객체를 돌려준다'''
for k in a.keys():
    print(k)
