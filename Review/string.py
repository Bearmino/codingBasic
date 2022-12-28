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
print(url_domain[-1])

