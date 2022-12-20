#파일 생성하기
f=open("새파일.txt", 'w')
f.close()
# 파일을 생성하기 위해서 파이썬 내장함수인 open을 사용"""
# open함수는 다음과 같이 "파일 이름"과 "파일 열기 모드"를 입력값으로 받고 결과값을 파일 객체로 돌려준다."""
# 파일객체 = open(파일이름, 파일열기모드)"""
# ------------------------------------------------------
# r : 읽기모드 - 파일을 읽기만 할 때 사용
# w : 쓰기모드 - 파일에 내용을 쓸 때 사용
# a : 추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬때 사용
# ------------------------------------------------------
f=open("c:/doit/새파일.txt",'w')
f.close()
# f.close()는 열려 있는 파일 객체를 닫아주는 역할(생략가능)

#파일 경로와 슬래시(/)
# """파이썬 코드에서 파일 경로를 표시할 때 슬래시(/)를 사용하며, 만약 역슬래시(\)를 사용시에는 역슬래시 2개(\\)하거나
# 문자열 앞에 r문자(Raw String)을 덧붙여 사용하면 좋다.

#파일을 쓰기 모드로 열어 출력값 적기
f=open("c:/doit/새파일.txt",'w')
for i in range(1,11):
    data="%d번째 줄입니다.\n" %  i
    f.write(data)
f.close()

#프로그램 외부에 저장된 파일을 읽는 다양한 방법
# 1. readline 함수 이용
f=open("c:/doit/새파일.txt",'r')
line = f.readline()
print(line)
f.close()
# f.open("새파일.txt",'r')로 파일을 읽기 모드로 연 후 readline()을 사용 후 첫 번째 줄을 읽음
f=open("c:/doit/새파일.txt",'r')
while True:
    line=f.readline()
    if not line:break
    print(line)
f.close()
# while문을 활용하여 모든 줄을 읽어올 수 있다.
f=open("c:/doit/새파일.txt",'r')
lines=f.readline()
for i in lines:
    line = line.strip() #줄 끝의 줄 바꿈 문자를 제거한다.
    print(line)
f.close()

# 2. read 함수 사용하기
f=open("c:/doit/새파일.txt",'r')
data = f.read()
print(data)
f.close()
# f.read()는 파일의 내용 전체를 문자열로 돌려준다.

#파일에 새로운 내용 추가하기
f=open("c:/doit/새파일.txt",'a')
for i in range(11,20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

#with문과 함께 사용하기
f=open("c:/doit/foo.txt",'w')
f.write("Life is too short, you need python")
f.close()
# 기존에는 해당 방식으로 열고 닫고를 진행했었야 했다.

with open("c:/doit/foo2.txt",'w') as f:
    f.write("Life is too short, you need python")
# 위와 같이 with문을 사용하면 with블록을 벗어나는 순간 열린 파일 객체 f가 자동으로 close 됨

#sys 모듈로 매개변수 주기
import sys

args = sys.argv[1:]
for i in args:
    print(i.upper(),end='')

