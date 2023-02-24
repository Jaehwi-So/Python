# 입출력 모드
# 1. r (read mode) : 읽기 전용 모드 (기본값)
# 2. w (write mode) : 쓰기 전용 모드
# 3. a (append mode) : 파일의 마지막에 새로운 데이터를 추가하는 모드

# 입출력 방식 모드
# 1. t (text mode) : 해당 파일의 데이터를 텍스트 파일로 인식하고 입출력함. (기본값)
# 2. b (binary mode) : 해당 파일의 데이터를 바이너리 파일로 인식하고 입출력함.

# 입출력 파일 모드
# 1. x (exclusive mode) : 열고자 하는 파일이 이미 존재하면 파일 개방에 실패함.
# 2. + (update mode) : 파일을 읽을 수도 있고 쓸 수도 있도록 개방함.

fp = open('./file/1.txt', 'rt+')
fp.close()

# 파일 읽기

# 전체 읽기
fp = open('./file/1.txt', 'r')
foo = fp.read()
print(foo)
foo = fp.read() # EOF까지 다 읽었으므로 읽어들일 것이 없음
print(foo)
fp.close()

# 한 라인 읽기
fp = open('./file/1.txt', 'r')
foo = fp.readline()
print(foo)
fp.close()

# 한 라인씩 전체 읽기
fp = open('./file/1.txt', 'r')
foo = fp.readlines() # 리스트 형태로 저장됨
print(foo)
fp.close()

# 파일 쓰기
fp = open('./file/2.txt', 'w')
fp.write('Hello World\n')
fp.close()

# 파일에 내용 추가하기
fp = open('./file/1.txt', 'a')
fp.write('\nHello World4')
fp.close()

# 자동으로 스트림 닫기
with open('./file/1.txt', 'r') as fp:
    foo = fp.read()
    print(foo)