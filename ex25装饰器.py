
#由于函数也是一个对象，而且函数对象可以被赋值给变量，
#所以，通过变量也能调用该函数。
def now():
	print('2015-3-25')
	return ''

f=now
print(f())

#函数对象有一个__name__属性，可以拿到函数的名字：
print(now.__name__)#now
print(f.__name__)#now
#现在，假设我们要增强now()函数的功能，
#比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
#这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

#本质上，decorator就是一个返回函数的高阶函数。
#所以，我们要定义一个能打印日志的decorator，可以定义如下：

def log(func):
	def wrapper(*args,**kw):
		print('call %s():'%func.__name__)
		return func(*args,**kw)
	return wrapper
#观察上面的log，因为它是一个decorator，
#所以接受一个函数作为参数，并返回一个函数。
#我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def now():
	print('2015-3-25')
	return ''

print(now())
#call now():
#2015-3-25


#如果decorator本身需要传入参数，
#那就需要编写一个返回decorator的高阶函数，写出来会更复杂。
#比如，要自定义log的文本：
def log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print('%s %s():'%(text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator

@log('自定义')
def now():
	print('2015-3-25')
	return '自定义log文本的循环嵌套\n' 

print(now())

#因为返回的那个wrapper()函数名字就是'wrapper'，所以，
#需要把原始函数的__name__等属性复制到wrapper()函数中，
#否则，有些依赖函数签名的代码执行就会出错。
#不需要编写wrapper.__name__ = func.__name__这样的代码，
#Python内置的functools.wraps就是干这个事的，
#所以，一个完整的decorator的写法如下：
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
	print('2015-3-25')
	return '完整的decorator\n'

print(now())

#或者针对带参数的decorator：
import functools
def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('%s %s():'%(text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator

@log
def now():
	print('2015-3-25')
	return '完整的decorator\n'

#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time,functools
def metric(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		t1=time.time()
		r=func(*args,**kw)
		print('%s excute in %s ms' %(func.__name__,1000*(time.time()-t1)))
		return r
	return wrapper

# 测试
@metric
def fast1(x, y):
    #time.sleep(0.0012)
    return x + y;

@metric
def fast2(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f1 = fast1(3,5)
f2 = fast2(3,5)
s = slow(4,5,6)
