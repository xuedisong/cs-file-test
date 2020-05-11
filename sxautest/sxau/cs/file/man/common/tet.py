# coding=utf-8
## 如果没有module名为te的实例，先把te实例化出一个实例，然后再运行该文件中的每一行代码，最后创建te变量指向该实例
## 若有，则新建变量te指向该实例。
# 被作为script的python文件，名称会先修改成丢失package信息的main module，然后执行一遍main module的静态代码。但是此类可能作为
# 原本名称的module 再被执行一遍静态代码（比如此module被import时）。所以将main module命名成__main__，且不要被引用（其实也不应该被引用，__main__的逻辑应该尽量简单）。
import te
print '运行tet'
if __name__ == '__main__':
    b = 5
    print 'main'

print 3

print 'main member={}'.format(dir())
