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

#While문 만들기
prompt="""
    1.Add
    2.Del
    3.List
    4.Quit

    Enter number:
"""
number = 0
while number !=4:
    print(prompt)
    number = int(input())

#while문 강제로 빠져 나오기
'''EX)자판기를 예시로 설명'''
coffe = 10
money = 300
while money:
    print("돈을 받았으니 커피가 나옵니다.")
    coffe = coffe -1
    print("남은 커피의 양은 %d입니다"% coffe)
    if coffe == 0:
        print("커피가 다 떨어져서, 판매를 중지합니다.")
    break
