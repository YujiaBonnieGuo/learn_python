# 看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。

# __slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。

# 除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

# __str__
# 我们先定义一个Student类，打印一个实例：
class Student(object):
    def __init__(self, name):
        self.name = name
print(Student('Michael1'))
# 打印出一堆<__main__.Student object at 0x109afb190>，不好看。

# 怎么才能打印得好看呢？只需要定义好__str__()方法，返回一个好看的字符串就可以了：
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
print(Student('Michael2'))
# __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，
# 也就是说，__repr__()是为调试服务的

# 再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，
# 所以，有个偷懒的写法：

class Student(object):
	def __init__(self,name):
		self.name=name
	def __str__(self):
		return 'Student object (name=%s)'%self.name
	__repr__=__str__
print(Student('Michael3'))


# __iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，
# 就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环
# 的下一个值，直到遇到StopIteration错误时退出循环。
# 我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：

class Fib(object):
	def __init__(self):
		self.a,self.b=0,1 # 初始化两个计数器a，b
	def __iter__ (self): 
		return self # 实例本身就是迭代对象，故返回自己
	def __next__ (self):
		self.a,self.b=self.b,self.a+self.b# 计算下一个值
		if self.a>100:# 退出循环的条件
			raise StopIteration()
		return self.a# 返回下一个值
#现在，试试把Fib实例作用于for循环：
for n in Fib():
	print(n)
print('\n','__getitem__')
# __getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，
# 但是，把它当成list来使用还是不行，比如，取第5个元素
# >>> Fib()[5]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'Fib' object does not support indexing
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib(object):
	def __getitem__(self,n):
		a,b=1,1
		for x in range(n):
			a,b=b,a+b
		return a

f=Fib()
print('the first number in Fib is: ',f[0])
#但是list有个神奇的切片方法：
print('slice of list',list(range(100))[5:10])
# 对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，
# 也可能是一个切片对象slice，所以要做判断：
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

#现在试试Fib的切片：
f=Fib()
print('slice of Fib: ',f[0:5])
#但是没有对step参数作处理：

print(f[:10:2],'\n')
# 也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。
# 此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，
# 例如str。
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，
# 还有一个__delitem__()方法，用于删除某个元素。
# 总之，通过上面的方法，我们自己定义的类表现得和Python自带的
# list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。

class Student(object):

    def __init__(self):
        self.name = 'Michael'
# 调用name属性，没问题，但是，调用不存在的score属性，就有问题了：

s = Student()
print(s.name)

# >>> print(s.score)
# Traceback (most recent call last):
#   ...
# AttributeError: 'Student' object has no attribute 'score'

#__getattr__
# 正常情况下，当我们调用类的方法或属性时，
# 如果不存在，就会报错

# 要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，
# 那就是写一个__getattr__()方法，动态返回一个属性。修改如下：

class Student(object):

    def __init__(self):
        self.name = 'Michael'
        
    def __getattr__(self, attr):
        if attr=='score':
            return 99
# 当调用不存在的属性时，比如score，
# Python解释器会试图调用__getattr__(self, 'score')
# 来尝试获得属性，这样，我们就有机会返回score的值：   
s=Student()
print(s.mame) 

print(s.score)  #return to 99

print(s.something_else)   #return to None
#返回函数也是完全可以的：
class Student(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25

#只是调用方式要变为：
s.age()
# 要让class只响应特定的几个属性，
# 我们就要按照约定，抛出AttributeError的错误：
class __getattr__(self,atter)