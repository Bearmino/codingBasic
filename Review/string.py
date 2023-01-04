# 1. letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
letters = 'Avatar'
print(letters[0],letters[2])

# 2. 자동차 번호가 하기와 같을 때 뒤에 4자리만 출력하세요.
license_palte='23가 0995'
print(license_palte[-4:])

# 3. 아래 문자열에서 '홀'만 출력하세요.
str = "홀짝홀짝홀짝"
print(str[::2]) # 슬라이싱 시작인덱스:끝인덱스:오프셋을 지정할 수 있습니다.

# 4. 문자열을 거꾸로 뒤집어 출력하세요.
str = "PYTHON"
print(str[::-1])

# 5. 아래의 전화번호에서 하이픈(-)을 제거하고 출력하세요. 하이픈 제거에서 숫자를 모두 붙여서 출력해보세요.
phone_number="010-1112-3334"
phone_number1 = phone_number.replace("-"," ") # 문자열에서 replace메서드를 사용하면 일부를 치환할 수 있다.문자열은 수정불가
print(phone_number1)
phone_number2 = phone_number1.replace(" ","")
print(phone_number2)

# 6. 하기 url에 저장된 웹 페이지 주소에서 도메인만 출력하세요.
url = "https://sharebook.kr"
url_domain = url.split(".") # split을 통해서 .을 기준으로 문자를 나눈다.
print(url_domain) # 리스트로 정렬
print(url_domain[-1])

# 7. 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
str = 'asbcdfe21a34a545a3'
str_up = str.replace('a','A')
print(str_up)

# 문자열 합치기,곱하기의 실행 결과를 예상해보기.
a="3"
b="4"
print(a+b)
# >>>34
print(a*3)
# >>>333 문자열에 대한 *는 문자열의 반복을 의미

# 8. 하기의 변수 문자열을 더하기와 문자열 곱하기를 활용하여 예의 문장처럼 출력하세요.
# 변수=t1,t2
# 실행 예 = python java python java python java python java
t1 = "python"
t2 = "java"
t3 = t1 + " " + t2 + " "
print(t3*4)

# 9. 하기와 같이 문자열과 정수가 바인딩 되어 있을때 %formatting을 사용해서 당음과 같이 출력해보세요.
# 이름: 김민수 나이: 10
# 이름: 이철희 나이: 13
name1="김민수"
age1=10
name2="이철희"
age2=13

print("이름: %s 나이: %d"%(name1,age1))
print("이름: %s 나이: %d"%(name2,age2))

# 10. 문자열의 format()메서드를 사용해서 9번 문제를 다시 풀어보세요.
print("이름: {} 나이: {}".format(name1,age1))
print("이름: {} 나이: {}".format(name2,age2))

# 11. 파이썬 3.6부터 지원하는 f-string을 사용해서 9번 문제를 다시 풀어보세요.
print(f'이름: {name1} 나이: {age1} ')
print(f'이름: {name2} 나이: {age2} ')

# 12. 하기의 숫자에서 컴마를 제거한 후 이를 정수타입으로 변환하세요.
# 숫자 = 5,148,579,618
num_str = "5,148,579,618"
num_str = num_str.replace(",","")
int(num_str)
print(num_str)

# 13. 하기의 문자열에서 2020/03만 출력하세요.
str = "2020/03(E) (IFRS연결)"
print(str[:7])

# 14. 하기의 문자열에서 좌우의 공백이 있을때 이를 제거해보세요.
str = "  삼성전자  "
str1 = str.strip()
print(str1)

# 15. 하기의 문자열이 있을 때 이를 대문자로 변경해보세요.
ticker = "btc_krw"
ticker1 = ticker.upper()
print(ticker1)
ticker2 = ticker1.lower()
print(ticker2) # 다시 소문자로

# 16. 문자열 'hello'를 'Hello'로 변경해보세요.
str = 'hello'
str1 = str.capitalize()
print(str1)

# 17. 하기와 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
ticker = "btc_krw"
ticker1=ticker.split("_")
print(ticker1)

# 18. 하기와 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
date = "2022-01-04"
date1 = date.split("-")
print(date1)

# 19. 하기 문자열에서 오른쪽 공백을 제거해보세요.
data = "0147451     "
data1 = data.rstrip(" ")
print(data1)

