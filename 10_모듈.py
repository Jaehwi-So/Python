import math #모듈 import
print(math.pi)

e = "hello"
from math import *  #전체 import
print(pi)
print(e) # 모듈의 오일러값과 변수명이 중복되어 선언한 변수를 사용할 수 없음

from math import pow # 일부 import
print(pow(2 ,2))