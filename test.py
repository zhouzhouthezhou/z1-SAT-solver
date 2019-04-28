from z1 import *

a = Bool('a')
b = Bool('b')

s = Solver()

#s.add('(a&~b)|~c')
#s.add(Or(And(a, Not(b)), Not(c)))
s.add(Imply(a, And(Not(a), Not(b))))

print(s.check())
print(s.model())
