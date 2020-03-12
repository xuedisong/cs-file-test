# -*- coding: utf-8 -*-
import a
from a import p

print 'p={}'.format(p)
p = 100
print 'a.p={}'.format(a.p)
print 'p={}'.format(p)
cl = a.f()
instance1=cl()
print ".....>........"
print 'dir(cl.mem)={}'.format(dir(cl.mem))
print 'type(cl.mem)={}'.format(type(cl.mem))
print 'cl.mem.__self__={}'.format(cl.mem.__self__)
print 'cl.mem={}'.format(cl.mem)

print 'dir(cl)={}'.format(dir(cl))
print 'dir(instance1.mem)={}'.format(dir(instance1.mem))
print 'instance1.mem.__self__={}'.format(instance1.mem.__self__)
print 'type(instance1.mem)={}'.format(type(instance1.mem))
print 'instance1.mem={}'.format(instance1.mem)
instance1.mem()
cl.mem(instance1)
print 'dir(instance1)={}'.format(dir(instance1))

instance1.counter = 1
print 'dir(instance1)={}'.format(dir(instance1))
while instance1.counter < 10:
    instance1.counter = instance1.counter * 2
print 'instance1.counter={}'.format(instance1.counter)
del instance1.counter
print 'dir(instance1)={}'.format(dir(instance1))