# _*_ encoding:utf-8 _*_
def foo(a):
    print "传来是对象的引用对象地址为{0}".format(id(a))
    a = 3 #形式参数a是局部变量，a重新绑定到3这个对象。
    print "变量a新引用对象地址为{0}".format(id(a))
    # print a

x = 5
print "全局变量x引用的对象地址为{0}".format(id(x))
foo(x)
print "变量x新引用对象地址为{0}".format(id(x))
print x
#由于函数内部a绑定到新的对象，也就修改不了全局变量x引用的对象5
# 全局变量x引用的对象地址为140462615725816
# 传来是对象的引用对象地址为140462615725816
# 变量a新引用对象地址为140462615725864
# 变量x新引用对象地址为140462615725816
# 5


def foo(a):
    """在函数内部直接修改了同一个引用指向的对象。
    也就修改了实际参数传来的引用值指向的对象。
    """
    a.append("can change object")
    return a

lst = [1,2,3]
print foo(lst)
print lst
#[1, 2, 3, 'can change object']
#[1, 2, 3, 'can change object']


def foo(a):
    """实际参数传来一个对象[1,2,3]的引用，当时形式参数
    （局部变量a重新引用到新的对象，也就是说保存了新的对象）
    当然不能修改原来的对象了。
    """
    a = ["python","java"]
    return a

lst = [1,2,3]
for item in foo(lst):
    print item
print lst
# python
# java