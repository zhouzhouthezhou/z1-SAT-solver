from z1 import *

####################################
#A says 'B is a Knave'
#B says 'Neither A nor I are Knaves'
####################################
#a -> !b
#b -> (a && b)
####################################
#a -> !m
#b -> a
#b -> b
####################################

a = Bool('a')
b = Bool('b')

s = Solver()

s.add(Imply(a,Not(b)))
s.add(Imply(b, a))
s.add(Imply(b, b))
#s.add(Imply(b, And(a, b)))
#s.add('~a|b')
#s.add('~b|(a&b)')
print('hello')
s.printConstraints()

print(s.check())
print(s.model())
