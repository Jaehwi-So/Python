# 에외 처리

try:
    var = 1
    # var = var / 0
    # raise IndexError
    print(var)
except ZeroDivisionError as e:
    print('0으로 나누기 불가능', e)
except Exception as e:
    print('예외 발생', e)
else:
    print("예외가 발생하지 않음")
finally:
    print("무조건 실행")