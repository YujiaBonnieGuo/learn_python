# 第一种方法简单直接粗暴有效，就是用print()把可能有问题的变量打印出来看看：
print('第一种方法：使用print打印')
def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n

def main():
    foo('10')

main()

# 用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息。所以，我们又有第二种方法。
# 断言
# 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代
print('\n\n')
print('第二种方法：用断言（assert）来替代print（ ）')
def foo(s):
    n=int(s)
    assert n !=0 ,'n is zero!'
    return 10/n

def main():
    foo('0')

# logging
# 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：
print('\n\n')
print('第三种方法：把print()替换为logging')
import logging
logging.basicConfig(level=logging.INFO)
s='0'
n=int(s)
logging.info('n=%d'%n)
print(10/n)
# 这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。

# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。
# 第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。我们先准备好程序：
# pdb
# 第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。我们先准备好程序：

# # err.py
# s = '0'
# n = int(s)
# print(10 / n)
# 然后启动：

# $ python -m pdb err.py
# > /Users/michael/Github/learn-python3/samples/debug/err.py(2)<module>()
# -> s = '0'
# 以参数-m pdb启动后，pdb定位到下一步要执行的代码-> s = '0'。输入命令l来查看代码：

# (Pdb) l
#   1     # err.py
#   2  -> s = '0'
#   3     n = int(s)
#   4     print(10 / n)
# 输入命令n可以单步执行代码：

# (Pdb) n
# > /Users/michael/Github/learn-python3/samples/debug/err.py(3)<module>()
# -> n = int(s)
# (Pdb) n
# > /Users/michael/Github/learn-python3/samples/debug/err.py(4)<module>()
# -> print(10 / n)
# 任何时候都可以输入命令p 变量名来查看变量：

(Pdb) p s
'0'
(Pdb) p n
0
输入命令q结束调试，退出程序：

# (Pdb) q
# 这种通过pdb在命令行调试的方法理论上是万能的，但实在是太麻烦了，如果有一千行代码，要运行到第999行得敲多少命令啊。还好，我们还有另一种调试方法。
# db.set_trace()
# 这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：
# err.py
print('\n\n')
print('第四种方法：pdb.set_trace()')
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)
