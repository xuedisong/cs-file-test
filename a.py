from sys import path
import sys

print sys.argv[0]
b = 0
c = 0
# 李鑫发放日的个人固定 g
if (b == 0):
    c = 3
    print c
print dir()
f4 = None


def f():
    global c
    print dir()
    b = 2
    b
    print 'local..'
    localName = "local name"
    print 'b:', b
    print 'local name:', localName
    b = 2
    print 'f.attr:'
    print dir()
    l1 = [1]

    def f1():
        global b
        print l1
        l1.append(2)
        print l1
        localName = "inner local name "
        print localName
        print dir()

    global f4
    f4 = f1
    # f1()
    print l1
    print localName
    print dir()
    return f1


l1 = [3]
f()
f4()
print 'global..'
print 'b:', b
