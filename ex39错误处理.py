# 在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码，这样，就可以知道是否有错，以及出错的原因。在操作系统提供的调用中，返回错误码非常常见。比如打开文件的函数open()，成功时返回文件描述符（就是一个整数），出错时返回-1。

# 用错误码来表示是否出错十分不便，因为函数本身应该返回的正常结果和错误码混在一起，造成调用者必须用大量的代码来判断是否出错：
def foo():
    r=some_function()
    if r==(-1):
        return (-1)
    #do something
    return r

def bar():
    r=foo()
    if r==(-1):
        print('Error')
    else:
        pass
#try

try:
    print('try...')
    r=10/0
    print('result: ',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('End the first try: ignore the wrong message 10/0\n')
# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
try:
    print('try...')
    r=10/2
    print('result: ',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('End the second try: run the right message 10/2\n')
