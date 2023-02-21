# 선언
def function1(a, b, c='+'):
    if c == '+':
        result = a + b
    elif c == '-':
        result = a - b
    elif c == '*':
        result = a * b
    elif c == '/':
        result = a / b
    else :
        result = None

    return result

print(function1(10, 20))
print(function1(a= 10, b= 20))
print(function1(10, 20, '-'))

# 가변 매개변수
def add(*numbers):  # *로 이용 튜플의 형태로 저장됨.
    result = 0
    for number in numbers:
        result += number
    return result

print(add(1,2,3,4,5))


# 가변 매개변수(key-value 형태)
def print_dic(**dicts):  # **로 이용
    for dic in dicts.items():
        print(dic)

print_dic(a=1, b=2)

# 복수 리턴값
def function2():
    return 1, 2

a, b = function2()
print(a, b)

# 람다식
# 일회성 익명 함수로 사용할 때 주로 사용. 단 한번밖에 사용할 수 없음
print((lambda a, b: a + b)(1, 2))


# 지역변수와 전역변수

def function3():
    global bar
    bar = "Hello" # Global 키워드로 재선언하면 전역 변수로 사용
    return

function3()
print(bar)

def function4():
    global foo  # global 키워드를 사용해야 지역 변수의 선언이 아닌 전역변수 변경을 할 수 있다.
    foo = "지역 변수" # 전역 변수의 값 변경
    print(foo)


foo = "전역 변수"
print(foo)  # 전역 변수
function4() # 지역 변수
print(foo)  # 지역 변수

