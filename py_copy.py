# 深拷贝，浅拷贝

import copy

a1 = [1,2,3]
a2 = (1,2,3)
a3 = [1,2,3,[4,5]]
a4 = [1,2,3, (4,5)]

b1 = copy.copy(a1)
c1 = copy.deepcopy(a1)
print(id(a1), id(b1), id(c1))
print([id(x) for x in a1],'\n',[id(x) for x in b1],'\n',[id(x) for x in c1])