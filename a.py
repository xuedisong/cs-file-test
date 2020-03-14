# coding=utf-8
import sys

'''

下层local scope修改上层 local scope的值没有捷径，除非引用到对象，那也是修改对象而已。

[1,2] == [1,2] True
[1,2] is [1,2] False # List 这种不是object的base type 需要 is来补充分辨地址相等

ClassA() ==/is ClassA() False
a=ClassA()
b=a
a is b False # not base type 不需要用is比较，就用相等即可。is反而不准确
a==b True  #此时，我理解比较地址值，所以相等

a1 = BClass()
a2 = BClass()
print a1.m3 == a2.m3 False
'''
print sys.argv[0]
b = 0
print dir()
f4 = None
p = 2
np = 44


def f():

    print 'lao 66={}'.format(sss)
    print 'dir={}'.format(dir())
    # 可以改变global name的值,所以本scope中的name其实是和global name一样的。所以一个东西不能处于两个namespace。本dir()就没有
    global np
    print np
    print 'dir={}'.format(dir())

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
        _field = 555

        # print 'wwwwwwwwwwwwwwwwww.............:'
        # exec 'print _field'
        def __init__(self):
            self.member = 'member'

        def mem2(self):
            print ''

        def mem(self):
            print 'mem.dir()={}'.format(dir())
            # print 'mem.__self__={}'.format(__self__)
            print self.member
            print self._field
            print self.mem2
            # global p
            print 'mem_p={}'.format(p)
            print 'mem_dir={}'.format(dir())

        print f4
        print 'adsfdsgsdgfdssg={}'.format(l12)

    def f1():
        # 先编译函数，把上一级local name 值拷贝到本scope  final 同名name,不会影响到上层local scope 的值。
        print 'f1dir={}'.format(dir())
        len(local_name)
        print 'f1dir={}'.format(dir())
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
sss=1000


class Dog:
    print 'class Dog={}'.format(__module__)


def f6():
    print 'f6={}'.format(dir())


f6()
print dir()
print p
print 'a end ........'
