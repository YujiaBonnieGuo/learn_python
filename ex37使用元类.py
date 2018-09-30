# type()
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。

# 比方说我们要定义一个Hello的class，就写一个hello.py模块：

class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

h = Hello()
print(h.hello())
print('type(h) is : ',type(h))
print('type(Hello) is : ',type(Hello))
# type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。

# 我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。

# type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：
def fn(self,name='world'):# 先定义函数
    print('Hello, %s'%name)

Hello=type('Hello',(object,),dict(hello=fn))# 创建Hello class

h=Hello()
print(h.hello())
print(type(Hello))#<class 'type'>
print(type(h))#<class '__main__.Hello'>
# 创建一个class对象，type()函数依次传入3个参数：

# 1.class的名称；
# 2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

# 定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
# 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass：
class MyList(list,metaclass=ListMetaclass):
    pass


#     当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

# __new__()方法接收到的参数依次是：

# 1.当前准备创建的类的对象；

# 2.类的名字；

# 3.类继承的父类集合；

# 4.类的方法集合。
#测试一下MyList是否可以调用add()方法：
L=MyList()
a=L.add(10)
print('L.add(10) : ',L)
