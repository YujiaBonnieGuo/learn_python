#List Comprehensions
#生成[1x1, 2x2, 3x3, ..., 10x10]
l=[]
for x in range(1,11):
	l.append(x**2)

print(l)

print([x**2 for x in range(1,11)])

#筛选出偶数的平方
print([x**2 for x in range(1,11) if x%2==0])

#以使用两层循环，可以生成全排列
print([m+n for m in 'ABC' for n in 'xyz'])

#列出当前目录下的所有文件和目录名
import os # 导入os模块，模块的概念后面讲到
print([d for d in os.listdir('.')])

#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in d.items():
	print(k,'=',v)

#列表生成式也可以使用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k+'='+v for k,v in d.items()])

#把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

#使用内建的isinstance函数可以判断一个变量是不是字符串
x = 'abc'
y = 123
print(isinstance(x, str))
print(isinstance(y, str))

#练习将混合list中的字符转换成小写
L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[s.lower() for s in L1 if isinstance(s,str) is True]
print(L2)
