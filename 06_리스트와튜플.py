# 리스트 선언
list1 = [1, 2, 3, 4, 5]
list2 = list((4, 5, 6, 7))

# 리스트 선택
print(list1[0])  # 1
print(list1[-1]) # 5

# 리스트 자르기 (원본 유지)
print(list1[2:4])    # [3 ,4]
print(list1[:3]) # [1, 2, 3]
print(list1[:]) # [1,2,3,4,5]

# 리스트 복사 (얕은 복사)
copy = list1
copy[4] = 6
print(copy, list1)   # 원본도 바뀜 [1,2,3,4,6]

# 리스트 복사 (깊은 복사)
copy2 = list1[:]
copy2[4] = 5    #리스트 슬라이싱을 통해 복사
print(copy2, list1)  # 원본은 유지

# 리스트 요소 추가, 제거
list1.append(5)  # 추가
list1.append(6)  # 추가
a = list1.remove(6)  # 제거, 인덱스가 가장 낮은 요소 하나 제거(값을 반환하지 않음)
print(list1, a) # [1,2,3,4,5,6], None

# 인덱스로 요소 추가, 꺼내기
list1.insert(0, 0)
print(list1)
a = list1.pop(6) #리스트의 해당 인덱스의 값 반환 및 제거
print(list1, a)

# 리스트 정렬
list1.reverse()  # 뒤집기
print(list1) # [5,4,3,2,1,0]
list1.sort() # 정렬
print(list1) # [0,1,2,3,4,5]

# 다차원 리스트
matrix = [[1,2,3], [4,5,6]]
print(matrix[0][1]) # 2

# 리스트 연산
print(list1 + list2)    # [0,1,2,3,4,5,4,5,6,7]
print(list1 * 2) # [0,1,2,3,4,5,0,1,2,3,4,5]
list1.extend(list2) # 연결하는 것은 같으나 원본을 변경시킴
print(list1) # [0,1,2,3,4,5,4,5,6,7]

# 튜플 : 리스트와 달리 값 변경 불가, 실행속도 빠름
tuple1 = (1, 2, 3, 4, 5)
tuple2 = 1, 2, 3
tuple3 = (1, )  # 요소를 하나만 가질 때에는 ,를 붙여주어야 파이썬이 튜플로 인식함

# 튜플 선택
print(tuple1[0])

# 튜플 자르기
print(tuple1[2:])   # (3, 4, 5)

# 튜플 연산
print(tuple1 + tuple3) # (1,2,3,4,5,1)

# 특정 요소 포함 여부
print(3 in tuple1)
print(7 in tuple1)
print(7 not in tuple1)

# 패킹과 언패킹
list3 = [2, 3, 4, 5]    # 패킹
a, b, c, d = list3  # 언패킹 : 구조분해할당과 비슷한 느낌. 길이가 일치해야 함
print(a, b, c, d)   # 2, 3, 4, 5

a, b, c, d, e = tuple1
print(a, b, c, d, e)

