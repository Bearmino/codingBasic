#딕셔너리(또는 해시(hash))란\
#딕셔너리는 Key와 Value를 한쌍으로 갖는 자료형
#ex) Key가 basebalss이라면 Value는 야구가 될 것이다.

#딕셔너리의 예제
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
#a[key]에 해당하는 {key:value}값이 쌍으로 삭제됨

#딕셔너리의 key 사용으로 Value값을 얻기
grade = {'peny':10,'donut':20,'mali':30}
print(grade['peny'])
print(grade['donut'])

#딕셔너리 만들 때 주의사항
a={1:'a',1:'b',1:'c'}
print(a)
#이렇게 key값이 중복될 경우에는 어떤 key값을 불러와야는지 알 수 없기에, 최종(key:value)값을 제외한 값은 무시한다

#딕셔너리 관련 함수
a={'name':'peny','phone':'011052547','birth':'1125'}
print(a.keys())
#a.keys()는 딕셔너리 a의 key만을 모아서 dict_keys라는 객체를 반환

for k in a.keys():
    print(k)
#dict_keys객체를 리스트로 변환 시 list 함수 사용
print(list(a.keys()))

#a.value()는 딕셔너리 a의 value값만을 모아서 dict_value라는 객체를 반환
print(a.values())

#key,value를 쌍으로 dict_items이라는 객체를 반환
print(a.items())

#key로 value값 얻기
print(a.get('name'))
print(a.get('phone'))

#존재하지 않는 키(nokey)로 접근하였을때에 none이라는 거짓이라는 뜻을 반환
print(a.get('nokey'))

#해당 key가 딕셔너리 안에 있는 조사는 value값 in 딕셔너리 객체로 확인 가능
print('name' in a)
print('pix' in a)

#key,value값 모두 지우기
a.clear()
print(a)

