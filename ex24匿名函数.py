#在Python中，对匿名函数提供了有限支持。
#还是以map()函数为例，计算f(x)=x2时，
#除了定义一个f(x)的函数外，还可以直接传入匿名函数：
a=list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(a)
#关键字lambda表示匿名函数，冒号前面的x表示函数参数。
#用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
#此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，
#再利用变量来调用该函数：
f=lambda x:x**2
#print(f)
print(f(5))
#同样，也可以把匿名函数作为返回值返回，比如：
from functools import reduce

def build(x, y):
    return lambda: x * x + y * y

c = build(2,3)()
print(c)

def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print(L)
#用匿名函数改造上面的代码
L = list(filter(lambda n: n%2==1, range(1, 20)))
print(L)