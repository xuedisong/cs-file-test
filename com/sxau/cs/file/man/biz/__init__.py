# coding=utf-8
b_data_member = 2
print ('asdgafhkasgfd')
'''
__all__ 定义后只会导入all中定义的 from xxx import __all__[0] 、[1]..
没有all定义时，会先创建出module（指from ..） 的实例，再把那个module 实例中的所有属性导入进去。
建议用from ... import ...
'''
__all__ = [ 'b_data_member']
