#print 출력을 담당
# 우리가 입력한 자료형의 출력을 담당한다.

a=123
print(a)
a="python"
print(a)

#큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일하다.
print("Life" "is" "too short")#1
print("Life"+"is"+"too short")#2

#문자열 띄어쓰기는 콤마로 한다.
print("Life","is","too short")

#한 줄에 결과값 출력하기
for i in range(10):
    print(i, end='')