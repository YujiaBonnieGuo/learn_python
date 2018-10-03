# 记录错误
# 如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。

# Python内置的logging模块可以非常容易地记录错误信息
# err_logging.py

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')
#样是出错，但程序打印完错误信息后会继续执行，并正常退出：
#通过配置，logging还可以把错误记录到日志文件里，方便事后排查。

#抛出错误
# 因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。

# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：


# err_raise.py
# class FooError(ValueError):
#     pass

# def foo(s):
#     n = int(s)
#     if n==0:
#         raise FooError('invalid value: %s' % s)
#     return 10 / n

# foo('0')


#执行，可以最后跟踪到我们自己定义的错误：
# Traceback (most recent call last):
#   File "ex40记录错误.py", line 40, in <module>
#     foo('0')
#   File "ex40记录错误.py", line 37, in foo
#     raise FooError('invalid value: %s' % s)
# __main__.FooError: invalid value: 0

# 只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型。

# 最后，我们来看另一种错误处理的方式：
print('\n\n\n\n\n另一种错误处理的方式:')
# err_reraise.py

def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' %s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise
bar()

# ValueError!
# Traceback (most recent call last):
#   File "ex40记录错误.py", line 72, in <module>
#     bar()
#   File "ex40记录错误.py", line 67, in bar
#     foo('0')
#   File "ex40记录错误.py", line 62, in foo
#     raise ValueError('invalid value: %s' % s)
# ValueError: invalid value: 0

# raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：

try:
    10/0
except ZeroDivisionError:
    raise ValueError('input error!')
