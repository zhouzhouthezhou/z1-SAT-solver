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
s.add(Imply(b, And(a, b)))

print(s.check())
print(s.model())
