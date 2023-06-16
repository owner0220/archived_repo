a = [1,2,3]
b=a
a[0]=38
print(id(a))
print(id(b))

a=[1,2,3]
b=a[:]
a[0]=38
print(id(a))
print(id(b))

import copy
a=[1,2,3]
b=copy.deepcopy(a)
a[0]=38
print(id(a))
print(id(b))