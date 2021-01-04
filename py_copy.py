# 深拷贝，浅拷贝

import copy

a1 = [1,2,3]
a2 = (1,2,3)
a3 = [1,2,3,[4,5]]
a4 = [1,2,3, (4,5)]

b1 = copy.copy(a1)
c1 = copy.deepcopy(a1)
b2 = copy.copy(a2)
c2 = copy.deepcopy(a2)
b3 = copy.copy(a3)
c3 = copy.deepcopy(a3)

b4 = copy.copy(a4)
c4 = copy.deepcopy(a4)


# print(id(a1), id(b1), id(c1))
# print([id(x) for x in a1],'\n',[id(x) for x in b1],'\n',[id(x) for x in c1])

# print(id(a2), id(b2), id(c2))
# print([id(x) for x in a2],'\n',[id(x) for x in b2],'\n',[id(x) for x in c2])

# print(id(a3), id(b3), id(c3))
# print([id(x) for x in a3],'\n',[id(x) for x in b3],'\n',[id(x) for x in c3])

print(id(a4), id(b4), id(c4))
print([id(x) for x in a4],'\n',[id(x) for x in b4],'\n',[id(x) for x in c4])