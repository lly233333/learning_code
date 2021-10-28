# reduce函数
from functools import reduce
r = reduce(lambda x, y: x + y, [1, 2, 3, 4], 10)
print(r)

# filter函数
f = list(filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(f)