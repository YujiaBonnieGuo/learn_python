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