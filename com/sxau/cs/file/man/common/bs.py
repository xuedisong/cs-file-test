# coding=utf-8
import b

class BsubClass(b.BClass):
    def m2(self):
        print self._mem1


a = 3
BsubClass().m2()
