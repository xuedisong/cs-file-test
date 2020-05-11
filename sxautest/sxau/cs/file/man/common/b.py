# coding=utf-8
class BClass:
    # 静态属性
    a = []
    _mb = 3
    _m4 = 4

    # 返回值是None
    def __init__(self):
        self._mem1 = 2

    # 非静态方法
    def m3(self):
        pass
        # print self._mem1

    # 静态属性,还是和实例挂钩，静态属性的一个动态实现tips
    @property
    def mb(self):
        self._mb = self._mb + 1
        self.a.append(self._mb)
        return self._mb

    @staticmethod # 也可以被classmethod替代达成目的。之后也方便扩展成classmethod。所以最小化原则，仅仅是想静态就用static
    def get_m4():
        return BClass._m4

    # # 构造方法重载
    # @staticmethod
    # def get_instance(bb):
    #     instance = BClass()
    #     instance._mb = bb
    #     return instance

    # 构造方法重载 自带静态，是类级别的
    @classmethod
    def m5(cls, ss):
        print 'cls={}'.format(ss)
        return ss

    # @staticmethod
    # def m51():
    #     temp = BClass()
    #     print 'temp={}'.format(temp)
    #     return temp


a1 = BClass()
a2 = BClass()

print BClass.get_m4()
# print BClass.get_instance('')
# print BClass.m51()
# f3 = BClass.m51
# f3()
print BClass.m5('lixinas')
print a1.m5('lixin')
