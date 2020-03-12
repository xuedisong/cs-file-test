# coding=utf-8
import sys

print sys.argv[0]
b = 0
print dir()
f4 = None
p = 2


def f():
    print '李先念:{}'.format(p)
    print dir()
    b = 2
    print 'local..'
    local_name = "local name"
    print 'b:', b
    print 'local name:', local_name
    b = 2
    print 'f.attr:'
    print dir()
    l12 = [1]

    class F1Class:
        """zky"""
        field = 555

        def __init__(self):
            self.member = 'member'

        def mem2(self):
            print ''

        def mem(self):
            print 'mem.dir()={}'.format(dir())
            # print 'mem.__self__={}'.format(__self__)
            print self.member
            print self.field
            print self.mem2
            #global p
            print 'mem_p={}'.format(p)
            print 'mem_dir={}'.format(dir())

        print f4
        print 'adsfdsgsdgfdssg={}'.format(l12)

    def f1():
        global b
        print 'b{}'.format(b)
        print l12
        l12.append(2)
        print l12
        local_name1 = "inner local name "
        print local_name1
        print dir()

    global f4
    f4 = f1
    # f1()
    print l12
    print local_name
    print dir()
    return F1Class


l1 = [3]
f()
f4()
print 'global..'
print 'b:', b


class Dog:
    print 'class Dog={}'.format(__module__)


def f6():
    print 'f6={}'.format(dir())


f6()
print dir()
print p
print 'a end ........'
