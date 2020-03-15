# import com.sxau as a
# import tet
#
# # a.__path__='zky'
# print 'lixin={}'.format(a.__path__)
#
# print dir(tet)
# print 2
#  [i for i in range(10)]
print '\n'.join([' '.join(['{}*{}={}'.format(i, j, i * j) for j in range(1, i + 1)]) for i in range(1, 10)])
