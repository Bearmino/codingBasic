#while문
'''반복해서 문장을 수행해야 할 경우 while문을 사용, 반복문이라고도 부른다.'''
'''while <조건문>
    <수행할 문장1>
    <수행할 문장2>
    <수행할 문장3>
'''
treeHits=0
while treeHits <10:
    treeHits = treeHits + 1
    print("나무를 %d번 찍었습니다."% treeHits)
    if treeHits == 10:
        print("나무 넘어갑니다.")