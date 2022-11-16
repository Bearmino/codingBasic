
## 파이썬 터틀 모듈을 가져오고 있다.
import turtle

## 그림을 그리기 위해서 캔버스(그리는 공간)을 불러온다.
t = turtle.Pen() ##Pen()을 부르는 함

## 캔버스의 마우스 형태의 그림을 거북이모양으로 변경하여 준다.
t.shape("turtle")

## 펜의 색상을 파란색으로 설정    
t.pencolor("blue")

## forward함수를 이용하여 직선으로 100pixel만큼 선을 그린다.
t.forward(100)
## right함수를 이용하여 90도만큼 방향을 바꾸어라.
t.right(90)
t.forward(100)

t.right(90)
t.forward(100)

t.right(90)
t.forward(100)
