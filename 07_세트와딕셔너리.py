# 세트
# 집합의 개념. 순서를 매길 수 없으며 중복값을 허용하지 않음

# 선언
set1 = {1, 1, 2, 3} # 1, 2, 3
set2 = {"Hello", "World"}
set3 = set("Hello")   # {'H', 'e', 'l', 'o'}
set3_2 = set([1,2,3,4,5])   # {1,2,3,4,5} set()의 인수로는 Iteratable Object
set4 = set() # 빈 Set, {}로 하면 딕셔너리로 인식


print(set1, set2, set3, set3_2, set4,)

# 요소 추가, 제거
set1.add(4)
print(set1) # {1,2,3,4}

set1.update((1, 6, 5))  #여러 개 추가
print(set1) # {1,2,3,4,5,6}

set1.remove(1)
print(set1) # {2,3,4,5,6}

# 집합 연산
set5= {1, 2, 3, 4, 5}
set6 = {4, 5, 6, 7}
print(set5 | set6)  # 합집합 {1, 2, 3, 4, 5, 6, 7}
print(set5 & set6)  # 교집합 {4, 5}
print(set5 - set6)  # 차집합 {1, 2, 3}
print(set5 ^ set6)  # 여집합 {1, 2, 3, 6, 7}




# 딕셔너리
# Key-Value 구조, Map이라고 보면됨

# 선언
# Key로는 문자열, 실수 등 이외에 튜플과 같은 변경 불가능한 타입의 값을 사용 가능(리스트, 딕셔너리 등 X)
dict1 = {"a": 1, "b": 2}
dict2 = dict({"a": 1, "b": 2})
dict3 = dict([('a', 1), ('b', 2)])
dict4 = dict(a=1, b=2)
dict5 = {}  # 빈 딕셔너리
print(dict1, dict2, dict3, dict4)

# 값 얻어오기
print(dict1.get('a'))   # 1
print(dict1['a'])   # 1
print(dict1.get('c'))   # None
# print(dict1['c'])  불가능

print(dict1.keys()) # 키목록 dict_keys(['a', 'b'])
print(dict1.values()) # 값목록 dict_values([1, 2])
print(dict1.items()) # 아이템(쌍)목록 dict_items([('a', 1), ('b', 2)])

keys = list(dict1.keys())   # 리스트로 변환
print(keys)

print('a' in dict1) # True : 키 포함 여부를 얻어옴
print(1 in dict1) # False

# 요소 추가, 제거
dict1['c'] = 3
del dict1['a']
print(dict1)    # {'b': 2, 'c': 3}
dict1.clear()
print(dict1)    # {}