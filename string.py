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

#이스케이프 코드
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

#문자열 슬라이싱
a="Life is too short, You need Phyton"
print(a[0:4])
"""a[0:4]가 뜻하는 것은 a 문자열의 0부터 4까지의 문자를 뽑아낸다는 뜻이다."""

#