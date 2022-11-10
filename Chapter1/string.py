#문자열로 표현 방법

print("Hello world")
print('Hello world')
print("""Phython is fun""")
print('''Phython is Life''')

#문자열에 작은 따옴표 포함 시키기
food = "Python's favorite food"
print(food)

#문자열에 큰 따옴표 포함 시키기
say = '"Phython is very easy".he say'
print(say)

#백슬러시(\)를 사용해서 작은,큰 따옴표 포함 시키기
tell = "Python \'s very simple"
print(tell)

#여러 줄인 문자열을 변수에 대입하고 싶을 때
multiLine1 = """
Life is too short
You need Python
"""
multiLine2 = '''
Life is too short
You need Python
'''
print(multiLine1)
print(multiLine2)

#이스케이프 코드!
'''프로그래밍할 떄 사용할 수 있도록 미리 정의해 둔 문자조합이다. 주로 출력물을 보기 좋게 정렬하는 용도활용'''
"""
\n 문자열 안에서 줄을 바꿀때 사용
\t 문자열 사이에 탭 간격을 줄 때 사용
\\ 문자 \를 그대로 표현할 때 사용
\' 작은따옴표(')를 그대로 표현할 때 사용
\" 큰따옴표(")를 그대로 표현할 때 사용
\r 캐리지 리턴(줄 바꿈 문자, 현재 커서를 가장 앞으로 이동)
\f 폼 피드(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)
\a 벨 소리(출력할 때 pc스피커에서 '삑'소리가 난다)
\b 백스페이스
\000 널문자
이 중에 확용빈도가 높은 것은 \n,\t,\\,\',\"이다. 
"""
#문자열 더해서 연결하기
head = "Python"
tail = " is fun!"
print(head+tail)

#문자열 곱하기
a="python "
print(a*2)

#문자열 곱하기 응용
print("="*50)
print("My Program")
print("=")

#문자열 길이 구하기
a="Life is too short"
print(len(a))

#문자열 인덱싱 및 활용
a="Life is too short, You need Phython"
print(a[3])
"""a[3]이 뜻하는 것은 a라는 문자열의 4번째 문자를 말한다. 모든 프로그래밍은 0부터 시작이다."""
print(a[0])

#인덱싱 활용하기
a="Life is too short, You need Phyton"
print(a[-1])
"""-1은 뒤에서부터 세어서 첫번째가 되는 문자를 말한다."""

#문자열 슬라이싱 및 활용
a="Life is too short, You need Phyton"
print(a[0:4])
"""a[0:4]가 뜻하는 것은 a 문자열의 0부터 4까지의 문자를 뽑아낸다는 뜻이다."""
print(a[0:5])
"""해당 부분에서는 공백도 포함하기에 공백부분까지 출력된다."""
print(a[19:])
"""끝부분을 삭제하면, 시작부분부터 문자의 끝까지를 출력한다."""
print(a[:17])
"""시작부분을 삭제하면, 처음부터 끝번호까지를 출력한다."""
print(a[:])
"""전체 문자열이 출력된다."""
print(a[19:-7])
"""a[19:-7]이 뜻하는 것은 a[19]에서부터 a[-8]까지를 말한다."""

#슬라이싱 활용하기
a="20010331Rainy"
year = a[:4]
date = a[4:8]
weather = a[8:]
print(year)
print(date)
print(weather)

#ex)Pithon이라는 문자열을 Python으로 변경하려면?
a="Pithon"
print(a[:1]+'y'+a[2:])

#문자열 포매팅
"""1. 숫자 바로 대입"""
a = "I eat %d apples." % 3
print(a)
'''문자열에 숫자를 넣고 싶은 자리에 %d문자를 넣어주고, 문장 가장 뒤에 삽입할 숫자를 % 뒤에 넣음 '''
'''%d는 문자열 포맷 코드라고 부른다.'''

"""2. 문자열 바로 대입"""
a = "I eat %s apples." % "five"
print(a)
'''문자열에 숫자 대신 문자열을 넣음'''

"""3. 숫자 값을 나타내는 변수로 대입"""
number =5
a= "I eat %d apples." % number
print(a)
'''변수를 통해서 대입'''

"""4. 2개 이상의 값 넣기"""
number = 10
day = "three"
a = "I ate %d apples.\nso I was sick for %s days" % (number,day)
print(a)

#문자열 포맷 코드
"""
%s 문자열(String)
%c 문자 1개(Character)
%d 정수(Integer)
%f 부동소수(Floating-point)
%o 8진수
%x 16진수
%% Literal (문자 %자체)
"""

#문자열 포맷 코드 이용
"""1. 정렬과 공백"""
a= "%10s" % "hi"
print(a)
'''오른쪽 정열로 10칸을 공백으로 채운 다음 문자열 표시'''

a="%-10sJane" % "hi"
print(a)
'''위와는 반대로 왼쪽 정렬로 10칸을 채운 후 문자열 표시  '''

"""2. 소수점 표현하기"""
a="%0.4f" % 3.421341
print(a)
'''3.421341를 소수점 4번째 자리까지만 나타내고 싶은 경우/ .의 경우에는 소수점 포인트이며 4는 소수점 뒤에 나올 갯수'''

#format 함수를 사용한 포매팅
"""format 함수를 사용하면 좀 더 발전된 문자열 포맷이 가능하다."""

"""1. 숫자 바로 대입하기"""
a="I eat {0} apples".format(3)
print(a)

"""2. 문자열 바로 대입하기"""
a="I eat {0} apples".format("five")
print(a)

"""3. 숫자 값을 가진 변수로 대입하기"""
number=3
a="I eat {0} apples".format(number)
print(a)

"""4. 2개 이상의 값 넣기"""
number=10
day="three"
a="I ate {0} apples.\nso I was sick for {1} days".format(number,day)
print(a)
a="I ate {number} apples.\nso I was sick for {day} days".format(number=10,day="three")
print(a)
'''위의 예제처럼 {0},{1}과 같은 인덱스 항목 대신 더 편리하게 {name}형태로 사용하는 방법도 있다.'''

"""5. 인덱스와 이름을 혼용해서 사용"""
a="I ate {0} apples.\nso sick for {day} days".format(5,day=10)
print(a)

"""왼쪽 정렬"""
a="{0:<10}".format("hi")
print(a)
'''오른쪽 정렬은 반대로 하면 된다.'''
a="{0:>10}".format("hi")
print(a)

"""가운데 정렬"""
a="{0:^10}".format("hi")
print(a)

"""공백 채우기"""
a="{0:=^10}".format("hi")
print(a)
a="{0:!<10}".format("hi")
print(a)

"""소수점 표현하기"""
y=3.42134234
a="{0:0.4f}".format(y)
print(a)

"""{ 또는 } 문자 표현하기"""
a="{{ and }}".format()
print(a)

#f 문자열 포매팅(가장 중요!!)
"""파이선 3.6버전부터 사용 가능하다."""
"""문자열 앞에 f접두사를 붙이면 f문자열 포매팅 기능을 사용할 수 있다."""
name='홍길동'
age=30
a=f'나의 이름은 {name}입니다.나이는 {age}입니다.'
print(a)
'''f 문자열 포매팅에서도 name,age와 같은 변수 값을 생성 후 참조가능, f 문자열 포매팅은 표현식을 지원'''
'''표현식이란?: 문자열 안에서 변수와 +, -와 같은 수식을 함께 사용 하는 것'''
age=30
a=f'나는 내년이면 {age+1}이 된다.'
print(a)

"""딕셔너리 f문자열 포매팅"""
a={'name':'홍길동','age':30}
print(f'나의 이름은 {a["name"]}이고, 나이는 {a["age"]}이다  ')

"""f 문자열에 대한 정렬"""
a=f'{"hi":<10}'
print(a) #왼쪽 정렬
b=f'{"hi":>10}'
print(b) #오른쪽 정렬   
c=f'{"hi":^10}'
print(c) #가운데 정렬

"""공백 채우기"""
a=f'{"hi":-^10}'
print(a)
b=f'{"hi":!<10}'
print(b)

"""소수점 채우기"""
y=3.4214721
a=f'{y:0.4f}' #소수점 4자리까지만 출력
print(a)
a=f'{y:10.4f}'
print(a)

"""f문자열에서 {}문자를 표기"""
a=f'{{and}}'
print(a)

#문자열 관련 함수들
"""문자열 자료형은 기본적으로 함수를 가지고 있다.(내장함수) 이 내장 함수를 사용하려면 문자열 변수 뒤에 '.'을 붙인 다음 함수 이름을 써주면된다."""

#문자 개수 세기(count)
a="hobby"
print(a.count('b'))

#위치 알려주기1(find)
a="python is the best choice"
print(a.find('b'))
print(a.find('j'))

#위치 알려주기2(index)
a="Life is too short"
print(a.index('t'))
# print(a.index('d'))
"""find와 index가 다른 점은 index의 경우 조건에 존재하는 문자가 없을 경우 에러를 발생시킨다."""

#문자열 삽입(join)
a=",".join("abcd")
print(a)

#소문자를 대문자로 변경(upper)
a="hi"
print(a.upper())

#대문자를 소문자로 변경(lower)
a="HI"
print(a.lower())

#오른쪽 공백 지우기(rstrip)
a=" hi "
print(a.rstrip())

#왼쪽 공백 지우기(lstrip)
a=" hi "
print(a.lstrip())

#양쪽 공백 지우기(strip)
a=" hi "
print(a.strip())

#문자열 바꾸기(replace)
a="Life is too short"
print(a.replace("Life","Young leg"))

#문자열 나누기(split)
a="Life is too short"
print(a.split())
b="a:b:c:d"
print(b.split(":"))
