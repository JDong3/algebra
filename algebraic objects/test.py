from matrix import *


v1, v2 = Vector([1, 2, 3]), Vector([3, 2, 1])
s = sum(v1, v2)
print(s.data)
p = product(s, 2)
print(p.data)