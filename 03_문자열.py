
# 문자형
# [", ', """, ''']
str = "Hello world"
print(type(str))

#여러줄 표현
str = """
hello
world
world
"""
print(str)

str = 'hello\nworld\nworld'
print(str)

str = "문자열1"
str2 = "문자열2"

# 문자열 붙이기
print(str + str2) # 문자열1문자열2
print(str * 3) # 문자열1문자열1문자열1
print(str, "그리고", str2) # 문자열1 그리고 문자열2

# 문자열에서 문자 선택
str = "Hello World"
print(str[2]) # l
print(str[-1]) # d
print(len(str)) # 11

# 문자열 자르기
print(str[6:11])    # World
print(str[6:])  # World
print(str[:5])  # Hello
print(str[2:-1])    # llo Worl

# 문자의 개수와 위치
print(str.count('l'))   # 3
print(str.find('e'))    # 1 (첫번째 인덱스)
print(str.index('ello'))   # 1 (첫번째 인덱스)
print(str.find('ze'))    # -1 (찾는 문자가 없을 시) <-> index()는 에러

# 대소문자 변환 (원본은 유지)
print(str.upper())  # HELLO WORLD
print(str.lower()) # hello world

# 문자열 치환 (원본은 유지)
print(str.replace("World", "Python"))   # Hello Python

# 문자열 나누기
print(str.split(' '))   # ['Hello', 'World']
print(str.split())  # ['Hello', 'World'] -> 인수가 없을 시 자동으로 white space를 기준으로 나눔
