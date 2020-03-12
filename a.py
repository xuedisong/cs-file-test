# coding=utf-8
import sys

print sys.argv[0]
b = 0
print dir()
f4 = None


def f():
    global c
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
    return f1


l1 = [3]
f()
f4()
print 'global..'
print 'b:', b
