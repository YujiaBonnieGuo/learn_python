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
def fn(self,name='world'):
    print('Hello, %s'%name)

Hello=type('Hello',(object,),dict(hello=fn))

h=Hello()
