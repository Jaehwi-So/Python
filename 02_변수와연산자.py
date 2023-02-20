
# 숫자형
number = 10
print(type(number)) # Class로 작성되어 데이터타입 제공

number2 = 10.12
print(type(number2))


# 부울형
isOK = True
print(type(isOK))

print(bool(1)) # True
print(bool(None)) # False

# 문자열, 튜플 딕셔너리 등이 비어있으면 False로 인식한다.
print(bool([1, 2, 3])) # True
print(bool([])) # False
print(bool({})) # False
print(bool('')) # False

# 논리연산자
value = (20 > 10) or (30 > 40)
print(value) # True
value = (not (20 > 10)) or (30 == 40)
print(value) # False


