#If문의 기본 구조
# if 조건문
#         수행할 문장1
#         수행할 문장2
#     else
#         수행할 문장A
#         수행할 문장B
#  테스트해서 참이면 if문 바로 다음 문장(if 블록)들을 수행하고, 조건문이 거짓이면 else문 다음 문장(else 블록)들을 수행하게 된다.
#  그러므로 else문은 if문 없이 독립적으로 사용할 수 없다.

money = True
if money:
   print("택시를 탑니다.")
else:
   print("걸어서 갑니다.")
#if조건문 다음 문항에서는 반드시 들여쓰기를 해야한다. 요즘 추세는 SPACE 4칸으로 진행하는게 추세다

#비교연산자
#(<,>,==,!=,>=,<=)'''
#EX) 만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어 가라
money = 2000
if money>=3000:
    print("택시를 타고 갑니다.")
else:
    print("걸어 갑니다.")

#and,or,not
#
# x or y : x와 y 둘중에 하나만 참이어도 참이다.
# x and y : x와 y 모두 참이어야 참이다.
# not x : x가 거짓이면 참이다.(반대로 설정하여 출력)
#
#EX) 돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어가라

card = True
if money >=3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# x in s, x not in s
# 다른 프로그래밍 언어에서는 쉽게 볼 수 없는 재미있는 조건문을 제공한다.
print(1 in [1,2,3])
print(1 not in [1,2,3])
print('a' in ('a','b','c'))
print('a' not in ('a','b','c'))

#EX) 만약 주머니에 돈이 있다면 택시를 타고, 없으면 걸어가라.
pocket = ['paper','cellphone','money']
if 'money' in pocket:
   print("택시를 타고 가라1")
else:
   print("걸어가라")

#조건문에서 아무 일도 하지 않게 설정하고 싶다면??
#해당 경우에는 pass를 사용하도록 하자
#EX) 주머니에 돈이 있으면 가만히 있고, 돈이 없으면 카드를 꺼내라'''
pocket = ["money","card"]
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

#다양한 조건을 판단하는 elIf
pocket = ['paper','handphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라2")
elif card:
    print("택시를 타고 가라3")
else:
    print("걸어가라")

#조건부 표현식
score = 10
if score >= 60:
    message = print("success!")
else:
    message = print("failure!")
# 위 코드를 파이썬의 조건 표현식으로 하면

message = "success1" if score >= 60 else "failure2"
print(message)