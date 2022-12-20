#pip
# pip은 파이썬 모듈이나 패키지를 쉽게 설치할 수 있도록 도와주는 도구이다.
# pip으로 파이썬 프로그램을 설치하면 의존성 있는 모듈 및 패키지를 함께 설치하기에 매우 편리하다.

#pip install
# PyPI(Python Package Index)는 파이썬 소프트웨어가 모인 저장 공간이다. 이곳에서 누구나 파이썬 패키지를 내려 받을 수 있다.
#pip install SomePackage    ←      최신버전으로 설치를 한다.
#pip install SomePackage==1.0.4     ←   1.0.4 특정 버전의 SomePackage를 설치
#pip install --upgrade SomePackage  ←   패키지를 최신 버전으로 업그레이드
#pip list   ←   pip를 이용하여 설치한 패키지 목록을 출력
#pip uninstall    ←     설치한 pip 패키지를 삭제

#Faker
# pip의 외부 라이브러리 중 하나로, faker는 테스트용 가짜 데이터를 생성할 때 사용하는 라이브러리이다.
# 하기와 같이 다량의 테스트 데이터등을 작성시 좀 더 편리한 방법으로 작성
#[(이름1,주소1),(이름2,주소2),.....(이름30,주소30)]
from faker import Faker
fake = Faker()
fake.name()
print(fake.name())
#>>>Corey Griffin   ←   Random으로 이름 생성

#만약 한글 이름이 필요하다면
fake = Faker('ko-KR')
print(fake.name())

#이름과 주소를 쌍으로 30건을 한다고 하면..
test_data = [(fake.name(),fake.address()) for i in range(30)]
print(test_data)
#>>>[('김지후', '강원도 서산시 개포가'), ('성춘자', '경기도 화성시 개포로'), .....







#faker
# fake.name()	    |   이름
# fake.address()	|   주소
# fake.postcode()	| 우편 번호
# fake.country()	|  국가명
# fake.company()	|  회사명
# fake.job()	    |  직업명
# fake.phone_number()	|   휴대 전화 번호
# fake.email()	    |   이메일 주소
# fake.user_name()	|   사용자명
# fake.pyint(min_value=0, max_value=100)    |   0부터 100 사이의 임의의 숫자
# fake.ipv4_private()   |	IP 주소
# fake.text()           |	임의의 문장 (한글 임의의 문장은 fake.catch_phrase() 사용)
# fake.color_name()	    |   색상명

#sympy
# 방정식 기호(symbol)를 사용하게 해주는 외부 라이브러리이다.


