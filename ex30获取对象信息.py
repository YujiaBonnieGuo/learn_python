#Type函数可以用来判断对象类型
print('the type of "123" is: ',type(123))
print('the type of "str" is: ',type('str'))
print('the type of "None" is: ',type(None))
#如果一个变量指向函数或者类，也可以使用type来判断
print('the type of function"abs" is: ',type(abs),'\n')

#但是type()函数返回对应的Class类型。
#如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：
print(type(123)==type(456))#True
print(type(123)==int)#True
print(type('abc')==type('123'))#True
print(type('abc')==str)#True
print(type('abc')==type(123),'\n')#False

#判断基本数据类型可以直接写int，str等，
#但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
import types
def fn():
	pass

print('type(fn)==types.FunctionType: ',type(fn)==types.FunctionType)
print('type(abs)==types.BuiltinFunctionType: ',type(abs)==types.BuiltinFunctionType)
print('type(lambda x: x)==types.LambdaType: ',type(lambda x: x)==types.LambdaType)
print('type((x for x in range(10)))==types.GeneratorType: ',type((x for x in range(10)))==types.GeneratorType,'\n')

#使用isinstance()
#定义一个animal的class

class Animal(object):
    pass

class Dog(Animal):
	pass

class Husky(Dog):
	pass

a = Animal()
d = Dog()
h = Husky()
print('isinstance(h, Husky)?: ',isinstance(h, Husky))
print('isinstance(h, Dog)?: ',isinstance(h, Dog))
print('isinstance(h, Animal)?:',isinstance(h, Animal))
print('isinstance(d, Husky)?: ',isinstance(d, Husky),'\n')

#能用type()判断的基本类型也可以用isinstance()判断：
print(isinstance('a', str))#True
print(isinstance(123, int))#True
print(isinstance(b'a', bytes),'\n')#True

print('isinstance([1, 2, 3], (list, tuple))?: ',isinstance([1, 2, 3], (list, tuple)))
print('isinstance((1, 2, 3), (list, tuple))?: ',isinstance((1, 2, 3), (list, tuple)))
# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

#使用dir()
#如果要获得一个对象的所有属性和方法，可以使用dir()函数，
#它返回一个包含字符串的list，
#比如，获得一个str对象的所有属性和方法：

print(dir('ABC'))

#类似__xxx__的属性和方法在Python中都是有特殊用途的，
#比如__len__方法返回长度。在Python中，
#如果你调用len()函数试图获取一个对象的长度，
#实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，
#下面的代码是等价的
print('the length of "ABC" is: ',len('ABC'))
print('ABC'.__len__())
#我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：

class MyDog(object):
	def __len__(self):
	    return 100

Bob=MyDog()
print(len(Bob))

#剩下的都是普通属性或方法，比如lower()返回小写的字符串：
print('ABc'.lower())

#仅仅把属性和方法列出来是不够的，配合getattr()、
#setattr()以及hasattr()，我们可以直接操作一个对象的状态
class myobject(object):
	def __init__(self):
		self.bob=9
	def power(self):
		return self.bob*self.bob

obj=myobject()

#紧接着，可以测试该对象的属性

print(hasattr(obj, 'bob') , '1.有属性bob吗？')
#has attribute
#判断一个对象里面是否有name属性或者name方法，返回BOOL值，
#有name特性返回True， 否则返回False。

print(hasattr(obj, 'y') , '2.有属性y吗？')

print(setattr(obj, 'y', 19) , '3.设置一个属性y')
#set attribute
#给对象的属性赋值，若属性不存在，先创建再赋值。
print(hasattr(obj, 'y') , '4.有属性y吗？')

print(getattr(obj, 'y') , '5.获取属性y')
#get attribute
#获取对象object的属性或者方法，如果存在打印出来，
#如果不存在，打印出默认值，默认值可选

print(obj.y , '6.获取属性y')

#如果试图获取不存在的属性，会抛出AttributeError的错误：
#>>> getattr(obj, 'z') # 获取属性'z'
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#AttributeError: 'MyObject' object has no attribute 'z'

#可以传入一个default参数，如果属性不存在，就返回默认值：

print('获取属性z，如果不存在，返回默认值404: ',getattr(obj, 'z', 404),'\n') 
# 获取属性'z'，如果不存在，返回默认值404

#也可以获得对象的方法：
print('有属性power吗?: ',hasattr(obj, 'power'))
print('获取属性power: ',getattr(obj, 'power'))
print('获取属性power并赋值到变量fn')
fn = getattr(obj, 'power')
print(fn())

# 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：

# sum = obj.x + obj.y
# 就不要写：

# sum = getattr(obj, 'x') + getattr(obj, 'y')
#一个正确的用法的例子如下：
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None

# 假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，
# 如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。

# 请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，
# 不代表该fp对象就是一个文件流，它也可能是网络流，
# 也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，
# 就不影响读取图像的功能。

