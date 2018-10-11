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
