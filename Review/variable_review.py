# 1. 삼성전자라는 변수로 50,000원을 바인딩 해보고, 만약 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
삼성전자=50000
평가금액=삼성전자*10
print("평가금액은 :",평가금액)

# 2. 변수 s와 t에는 각각 하기처럼 바인딩이 있었습니다. 두 변수를 시가총액,현재가,PER등을 바인딩 해보세요.
# 시가총액 >	29억
# 현재가	 >   50,000원
#  PER	 >   15.79
시가총액 = 2900000000
현재가 = 50000
PER = 15.79
print(시가총액,type(시가총액))
print(현재가,type(현재가))
print(PER,type(PER))

# 3. 변수 s와 t에는 각각 문자열이 두 변수를 활용하여 아래 예제처럼 바꾸어 보세요.
s = "Hello"
t = "Python"
# 출력 : Hello!! Python
print(s+"!! ",t)

# 4. 2+2*3의 코드 실행 결과를 출력하세요.
print(2+2*3)

# 5. a="132"의 변수 a는 어떤 타입인지 판별해보세요.
a="132"
print(type(a))

# 6. num_str="720"인 문자열을 정수로 치환하여 보세요.
num_str="720"
num_str = int(num_str)
print(num_str,type(num_str))

# 7. 정수 100을 문자열 100으로 치환하여 보세요.
num = 100
num = str(num)
print(num,type(num))

# 8. 문자열 "15.79"를 실수(float)타입으로 치환하여 보세요.
num_float = "15.79"
num_float = float(num_float)
print(num_float,type(num_float))

# 9. year라는 변수가 문자열 타입의 연도 2020을 바인딩하고 있다. 이를 정수로 변환 후 최근 3년 연도를 화면에 출력하시오.
year = "2020"
year = int(year)
print(year)
print(year-3, year-2, year-1)

# 10. 에어컨이 월 48,584원으로 무이자 36개월로 구매하였다. 변수를 사용하여 총금액을 구해 보세요.
air_month = 48584
period = 36
result = air_month*period
print(result)