#For문(반복문)의 기본구조
'''
for 변수 in 리스트(또는 튜플,문자열):
    수행할 문장1
    수행할 문장2

'''

#전형적인 for문
test_list = ['one','two','three']
for i in test_list:
    print(i)
'''리스트의 첫 번째 요소인 'one'이 먼저 i 변수에 대입된 후 print(i)를 출력한다. '''

#다양한 for문의 사용
a=[(1,2),(3,4),(5,6)]
for(first,last) in a:
    print(first + last)
'''a리스트의 요솟값이 튜플로 각 요소가 자동으로 (first,last)변수에 대입된다.'''
'''해당 부분은 tuple에서 (first,last) = (1,2)와 비슷한 방법이다.'''

#for문 응용
'''EX) 총 5명의 학생이 시험을 보았으며, 시험점수가 60점을 넘기면 "합격" 그렇지 않으면 "불합격"이다. '''
marks = [90,25,35,80,70]

number=0
for mark in marks:
    number+=1
    if mark >=60:
        print("%d번 학생은 합격 입니다" % number)
    else:
        print("%d번 학생은 불합격 입니다."% number)

#for문과 continue
marks = [100,40,50,70,30]

number = 0
for mark in marks:
    number+=1
    if mark<60:
        continue
    else:
        print("%d번째 학생 합격을 축하합니다."% number)

#for문과 함께 자주 사용하는 range 함수
a=range(10)
print(a)
'''range(10)은 0부터 10미만의 숫자를 포함하는 range 객체를 만들어 준다.'''
'''시작 숫자와 끝 숫자를 지정하려면, range(시작숫자, 끝숫자)형태를 사용, 이때 끝 숫자는 포함되지 않는다.'''

#range 함수의 예시 살펴보기
add=0
for i in range(1,11):
    add+=i
    print(add)

marks = [90,80,50,40,70]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    else:
        print("%d번 학생은 합격을 축하드립니다." % (number+1))
'''len함수는 리스트 안ㄴ의 요소 갯수를 돌려주는 함수로, .len(marks)는 5가 될 것이고, range(len(marks)는 range(5)다 '''

#for와 range를 이용한 구구단
for i in range(2,10):
    for j in range(1,10):
            print(i*j,end=" ")
    else:
        print(' ')