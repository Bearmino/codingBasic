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
        print("%d번 학생은 합격입니다" % number)
    else:
        print("%d번 학생은 불합격입니다."% number)
