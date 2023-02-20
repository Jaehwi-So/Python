# While
i = 0
while i < 10 :
    print(i)
    i = i + 1

# for-in
# 문자열, 튜플, 리스트 순회
arr = ["사과", "딸기", "수박"]
for j in arr :
    print(j)

str = "안녕하세요"
for j in str :
    print(j)

# for-in-range
for col in range(2, 10):    # 2~9
    for row in range(1, 10):
        print(col, "x", row, "=", col * row)

# break, continue
for num in range(1, 20):    # 1 3 5 7 9
    if(num > 10) :
        break
    if((num % 2) == 0) :
        continue
    print(num)