import textwrap

#textwrap.shorten()
# textwrap.shorten() 함수는 매개변수 width로 전달한 길이만큼 문자열을 줄여 표시한다.
long_text = 'Life is too short, you need python'
shor_text = textwrap.shorten(long_text, width=15)
print(shor_text) # Life is [...] , 축약된 문자열임을 뜻하는 [...]
shor_text_place = textwrap.shorten(long_text, width=15, placeholder='...중략...')
print(shor_text_place) # Life is...중략..., placeholder 인자를 설정하면 생략 표시 문자열을 지정할 수 있다.

#textwrap.wrap()
# textwrap.wrap()은 긴 문자열을 원하는 길이로 줄 바꿈(wrapping)할 때 사용하는 함수이다.

long_text = 'Winners embrace hard work. They love the discipline of it, the trade-off theyre making to win. ' \
            'Losers, on the other hand, see it as punishment. And that’s the difference.'
shor_text = textwrap.wrap(long_text, width=50)
print(shor_text)
print('\n'.join(shor_text))