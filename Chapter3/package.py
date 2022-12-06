#[패키지란 무엇인가?]
#  패키지느 도트(.)를 사용하여 파이썬 모듈을 계층적(디렉터리)구조로 관리할 수 있게 해준다.
#  ex) 모듈 이름이 A.B인 경우에 A는 패키지 이름이 되고 B는 A패키지의 B모듈이 된다.
#
# 가상 game패키지
# game/
#  __init__.py
#     sound/
#         __init__.py
#         echo.py
#         wav.py
#     graphic/
#         __init__.py
#         screen.py
#         render.py
#     play/
#         __init__.py
#         run.py
#         test.py
# game,sound,graphic,play는 디렉터리이고 .py인 파일은 파이썬 모듈이다.
# game디렉터리가 root이며, sound,graphic,play는 서브 디렉터리이다.
# 패키지 구조로 파이썬 프로그램을 만드는 것이 공동 작업이나 유지보수등에서 유리하며, 다른 모듈과 이름이 겹치더라도 안전하게 사용가능

#[패키지 만들기]
# 1. C:/doit 디렉터리 밑에 game 및 기타 서브 디렉터를 생성 및 .py파일들을 생성한다.
#   C:/doit/game/__init__.py
#   C:/doit/game/sound/__init__.py
#   C:/doit/game/sound/echo.py
#   C:/doit/game/graphic/__init__.py
#   C:/doit/game/graphic/render.py
#
# 2. 각 디렉터리에 __init__.py파일을 만들어 놓기만 하고 내용은 빈 상태로 둔다.
# 3. echo, reder .py 파일을 다음과 같이 만든다.
#  #echo.py
#     def echo_test():
#        print("echo")
#  #redner.py
#     def render_test():
#        print("render")
# 4. 예제를 수행하기 전에 우리가 만든 game패키지를 참조할 수 있도록 명령 프롬프트 창에서 set명령어로 PYTHONPATH환경변수에
#    C:/doit 디렉터리를 추가한다. 그리고 파이썬 인터프리터(interactive shell)를 실행한다.
#  C:\> set PYTHONPATH = C:/doit
#  C:\> python
#  Type "help", "copyright", "credits" or "license" for more information
#
#[패키지안의 함수를 실행하기]
# 패키지를 사용하여 echo.py파일의 echo_test함수를 실행하여 보자.
# 다름 예제는 import예제로 하나의 예제를 실행 후 다음 예제를 실행 시 반드시 인터프리터를 종료후 다시 실행한다.
#
# 1. echo 모듈은 echo.py 파일이다.
# >>> import game.sound.echo
# >>> game.sound.echo.echo_test()
# echo
#
# 2. echo 모듈이 있는 디렉터리까지를 from...import하여 실행하는 방법
# >>> from game.sound import echo
# >>> echo.echo_test()
# echo
#
# 3. echo모듈의 echo_test 함수를 직접 import하여 실행하는 방법
# >>> from game.sound.echo import echo_test
# >>> echo_test()
# echo

#[__init__.py의 용도]
#__init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다.
#python3.3버전부터는 __init__.py파일이 없어도 패키지로 인식을 하지만, 하위 호환을 위해 생성하는 것이 안전하다.

#[relative 패키지]
#만약 graphic 디렉터리의 render.py모듈이 sound 디렉터리의 echo.py모듈을 사용하고 싶다면.
# #render.py을 수정
# from game.sound.echo import echo_test
# def render_test():
#   print("render")

#echo_test를 추가하여 echo_test함수를 사용할 수 있도록 수정하였다.
#>>>from game.graphic.render import echo_test
#>>>render_test()
#render
#echo

#위의 예제처럼 from game.sound.echo import echo_test를 입력해 전체 경로를 사용도 가능하지만,
#realative하게 import 사용도 가능하다.

# #render.py
# from..sound.echo import echo_test
# def render_test():
#   print("render")
#   echo_test()

# .. 은 render.py파일의 부모 디렉터리를 의미한다. 따라서 render.py파일의 부모 디렉터리는 game이므로 위처럼 import가 가능

# .. -> 부모 디렉터리
# .  -> 현재 디렉터리




