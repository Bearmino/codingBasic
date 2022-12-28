# 정규 표현식(정규식)
# 복잡한 문자열을 처리할 때 사용하는 기법으로, 파이썬만의 고유 문법이 아니라 문자열을 처리하는 모든 곳에서 사용한다.

# 정규식이 필요한 이유?
# 예를들어, 주민등록번호를 포함하고 있는 텍스트가 있다. 이 텍스트에 포함된 모든 주민등록번호의 뒷자리를 *문자로 변경한다고 하자.

# 정규식을 모른다고 하면,
# 1. 전체 텍스트를 공백 문자로 나눈다(split)
# 2. 나뉜 단어가 주민등록번호 형식인지 조사한다.
# 3. 단어가 주민등록번호 형식이라면 뒷자리를 *로 변환한다.
# 4. 나뉜 단어를 다시 조립한다.
data = """
park 800905-1049118
kim  700905-1059119
"""

result = []
for line in data.split("\n"):
    word_result=[]
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6]+"-"+"******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))
#>>>park 800905-******
#   kim  700905-******

# 반면 정규식을 사용하게 된다면,
import re

data ="""
park 800905-1049118
kim  700905-1059119
"""

pat=re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******",data))
#>>>park 800905-******
#   kim  700905-******

# 정규 표현식의 기초, 메타문자
# 정규 표현식에서 사용하는 메타문자는 .^$*+?{}[]\|()가 있다.(메타문자는 그 문자가 가진 뜻이 아닌 특별한 용도로 사용하는 문자)

# 문자클래스 []
# "[]사이의 문자들과 매치"라는 의미를 갖는다.(※문자 클래스를 만드는 메타 문자인 []사이에는 어떤 문자도 들어갈 수 있다.)
# 예를들어, 정규표현식이 [abc]라면 이 표현식의 의미는 "a,b,c 중 한개의 문자와 매치"를 뜻한다.
#
#   - "a"는 정규식과 일치하는 문자인 "a"가 있으므로 매치
#   - "before"는 정규식과 일치하는 문자인 "b"가 있으므로 매치
#   - "dude"는 정규식과 일치하는 문자인 a,b,c중 어느 하나도 포함하고 있지 않으므로 매치되지 않음
#
# []안의 두 문자 사이에 하이픈(-)을 사용하면 두 문자 사이의 범위(From-To)를 의미한다.
# 예를들어 [a-c]라는 정규 표현식은 [abc]와 동일하고 [0-5]는 [012345]와 동일하다.
#
#   - [a-zA-Z]:알파벳 모두
#   - [0-9]:숫자
#
# 주의)문자 클래스[]안에서는 어떤 문자나 메타 문자도 사용할 수 있지만, ^문자는 주의해야한다.
# ^메타 문자를 사용의 겨이우 반대(not)이라는 의미를 갖는다.
# 예를 들어, [^0-9]라는 정규 표현식의 경우 숫자가 아닌 문자만 매치된다.
#
# 자주 사용하는 문자 클래스
# \d - 숫자와 매치,[0-9]와 동일한 표현식이다.
# \D - 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.
# \s - whitespace 문자와 매치, [\t\n\r\f\v]와 동일한 표현식 (맨앞의 빈 칸은 공백문자(space)를 의미한다.
# \w - 문자 + 숫자(alphanumeric)와 매치, [a-zA-Z0-9]와 동일한 표현식이다.
# \W - 문자 + 숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9]와 동일한 표현식이다.


# Dot(.)
# 정규 표현식의 Dot(.)메타 문자는 줄바꿈 문자인 \n을 제외한 모든 문자와 매치됨을 의미한다.
# a.b라는 정규식의 의미는 "a+모든문자+b"이다. 즉 a와 b라는 문자 사이에 어떤 문자가 들어가도 모두 매치가 된다는 의미이다.
# 예를 들어, "aab","a0b","abc"가 정규식 a,b와 어떻게 매치되는지 보자.
#
#   - "aab"는 가운데 문자 "a"가 모든 문자를 의미하는 .과 일치하므로 정규식과 매치된다.
#   - "a0b"는 가운데 문자 "0"가 모든 문자를 의미하는 .과 일치하므로 정규식과 매치된다.
#   - "abc"는 "a"문자와 "b"문자 사이에 어떤 문자라도 하나는 있어야하는 이 정규식과 일치하지가 않음으로 매치되지 않는다.
#
# a[.]b라는 정규식의 의미는 "a+Dot(.)문자+b"이다.따라서, "a.b"문자열과는 매치되고, "a0b"문자열과는 매치되지 않는다.
# 주의) 문자 클래스([])내에 Dot(.)메타 문자가 사용된다면 이것은 "모든문자"라는 의미가 아닌 문자 .그대로를 의미한다.
#
#
# 반복(*)
# 정규 표현식의 *메타 문자는 * 바로 앞에 있는 문자 a가 0부터 무한대로 반복될 수 있다는 의미이다.
# 사실상은 무한대가 아니라 2억개 미만 정도만 가능하다.
# 정규식  |	문자열     |   Match 여부	    |       설명
# ca*t	 |    ct	  |      Yes	    |   "a"가 0번 반복되어 매치
# ca*t	 |   cat	  |      Yes	    |   "a"가 0번 이상 반복되어 매치 (1번 반복)
# ca*t	 |  caaat     |	     Yes	    |   "a"가 0번 이상 반복되어 매치 (3번 반복)
#
#
# 반복(+)
# 반복을 나타내는 또다른 메타 문자로 +는 최소 1번 이상 반복될 때 사용한다. 즉 *가 반복횟수 0번이면, +는 반복횟수 1부터인것이다.
# 정규식 |	문자열	   Match 여부     |	    설명
# ca+t	|   ct	    |    No	         |  "a"가 0번 반복되어 매치되지 않음
# ca+t	|   cat	    |    Yes	     |  "a"가 1번 이상 반복되어 매치 (1번 반복)
# ca+t	|   caaat	|    Yes	     |  "a"가 1번 이상 반복되어 매치 (3번 반복
#
#
# 반복({m,n},?)
# {}메타 문자를 상용하면 반복 횟수를 고정할 수 있다. {m,n}정규식을 사용하면 반복 횟수가 m부터 n까지 매치할 수 있다.
# {}을 사용한 몇 가지 정규식을 살펴보자.
# 1.{m}
#   ca{2}t
#   "c+a(반드시 2번 반복)+t"
#       정규식  |  문자열  |	Match 여부   |	         설명
#       ca{2}t |   cat	 |     No       |	"a"가 1번만 반복되어 매치되지 않음
#       ca{2}t |   caat	 |     Yes	    |     "a"가 2번 반복되어 매치
#
# 2.{m,n}
#   ca{2,5}t
#   "c+a{2~5회 반복}+t"
#      정규식  |	  문자열	 |   Match 여부	|           설명
#    ca{2,5}t |	  cat	 |      No	    |   "a"가 1번만 반복되어 매치되지 않음
#    ca{2,5}t |	  caat	 |     Yes	    |   "a"가 2번 반복되어 매치
#    ca{2,5}t |	caaaaat	 |     Yes	    |   "a"가 5번 반복되어 매치
#
# 3.?
#  반복과 관련된 부분은 아니지만, 비슷한 개념으로 {0,1}을 의미한다.
#   ab?c
#   "a+b(있어도 되고 없어도 된다.)+c"
#      정규식  |	  문자열   |	 Match 여부   |	        설명
#       ab?c  |	   abc	  |      Yes	 |    "b"가 1번 사용되어 매치
#       ab?c  |	    ac	  |      Yes	 |    "b"가 0번 사용되어 매치
#
# 파이썬에서 정규 표현식을 지원하는 re모듈
# 정규 표현식을 지원하기 위해 re(regular expression)모듈을 제공한다.(파이썬 설치시 자동 설치)
# Sample)
# import re
# p=re.compile('ab*')
# re.complie을 사용하여 정규 표현식(ab*)을 컴파일 한다. re.complie의 결과로 돌려주는 객체p(컴파일된 패턴 객체)를
# 사용하여 그 이후의 작업 수행
#
# 정규식을 이용한 문자열 검색
#   Method	|               목적
# match()	|   문자열의 처음부터 정규식과 매치되는지 조사한다.
# search()	|   문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
# findall()	|   정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴한다.
# finditer()|  	정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 리턴한다.
#
import re
p = re.compile('[a-z]+')

# match
# 정규식의 검색 결과로 리턴된 객체를 말함(match 또는 None을 리턴함)
m = p.match("python")
print(m)
#>>> <re.Match object; span=(0, 6), match='python'>
# "python"문자열은 [a-z]+정규식에 부합되어 match객체를 돌려준다.

m = p.match("3 python")
print(m)
# "3 python"문자열의 첫 문자이 3이 정규식[a-z]+에 부합되지 않아서 None을 돌려준다.

p = re.compile('here')
m = p.match('string goes here')
if m:
    print('Match found: ',m.group())
else:
    print('No match')

# match 객체의 메서드
#  메서드  |	        목적
# group() |	매치된 문자열을 돌려준다.
# start() |	매치된 문자열의 시작 위치를 돌려준다.
# end()	  |  매치된 문자열의 끝 위치를 돌려준다.
# span()  |	매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다.

p = re.compile('[a-z]+')
m = p.match("python")
print(m.group())
# >>> python
print(m.start())
# >>> 0
print(m.end())
# >>> 6
print(m.span())
# >>> (0,6)

# search
p = re.compile('[a-z]+')
m = p.search("3 python")
print(m)
# >>> <re.Match object; span=(2, 8), match='python'>
# "3 python" 문자열의 첫 번째 문자는 "3"이지만 search는 문자열의 처음부터 검색하는 것이 아닌 문자열
# 검색하기 때문에 "3"이후의 "python"문자열과 매치된다.

# findall
result = p.findall("life is too short")
print(result)
# >>> ['life', 'is', 'too', 'short']
# findall은 패턴([a-z]+)과 매치되는 모든 값을 찾아 리스트로 리턴한다.

# finditer
# findall과 동일하지만 그 결과로 반복 가능한 객체(iterator object)를 리턴한다.
result = p.finditer("life is to short")
print(result)
# >>> <callable_iterator object at 0x0000020CAF02CD00>
for i in result: print(i)
# >>><re.Match object; span=(0, 4), match='life'>
# <re.Match object; span=(5, 7), match='is'>
# <re.Match object; span=(8, 10), match='to'>
# <re.Match object; span=(11, 16), match='short'>

# 모듈 단위로 수행하기
# 지금까지 re.compile을 사용하여 컴파일된 패턴 객체로 그 이후 작업을 수행했다.
# re모듈은 이것을 보다 축약한 형태로 사용할 수 있는 방법이 있다.
p = re.compile('[a-z]+')
m = p.match("python")
# 위 코드를 축약하면...
m = re.match('[a-z]+',"python")
print(m)

# 컴파일 옵션
# 정규식을 컴파일 시 다음 옵션을 사용할 수 있다.
# DOTALL(S) - . 이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.
# IGNORECASE(I) - 대소문자에 관계없이 매치할 수 있도록 한다.
# MULTILINE(M) - 여러줄과 매치할 수 있도록 한다. (^, $ 메타문자의 사용과 관계가 있는 옵션이다)
# VERBOSE(X) - verbose 모드를 사용할 수 있도록 한다. (정규식을 보기 편하게 만들수 있고 주석등을 사용할 수 있게된다.)

# DOTALL,S
# .메타 문자는 줄바꿈 문자(\n)를 제외한 모든 문자와 매치되는 규칙이 존재
# \n문자도 포함하여 매치하고 싶다면 re.DOTALL 또는 re.s옵션을 사용해 정규식을 컴파일하면 된다.
p = re.compile('a.b')
m = p.match('a\nb')
print(m)
# >>> None
p = re.compile('a.b',re.DOTALL)
m = p.match('a\nb')
print(m)
# >>> <re.Match object; span=(0, 3), match='a\nb'>
