#计算一个list【1-9】的平方【1-81】
def f(x):
	return x**2
#用map的iterator实现
r=map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))
#用循环实现
l=[]
for n in [1,2,3,4,5,6,7,8,9]:
	l.append(f(n))
print(l)
#将1-9转化为字符
print(list(map(str,[1,2,3,4,5,6,7,8,9])))
#可以用reduce实现对一个序列求和
from functools import reduce
def add(x,y):
	return x+y

print(reduce(add,[1,3,5,7,9]))
#把序列[1, 3, 5, 7, 9]变换成整数13579
from functools import reduce
def fn(x,y):
	return x*10+y
print(reduce(fn,[1,3,5,7,9]))
#配合map()，我们就可以写出把str转换为int的函数
from functools import reduce
def fun(x,y):
	return fn(x,y)

def char2num(s):
	digits={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	return digits[s]

print(reduce(fn,map(char2num,'13579')))
#还可以用lambda函数进一步简化成：
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
	return DIGITS[s]
def str2int(s):
	return reduce(lambda x,y:x*10+y,map(char2num,s))

#第一题：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def FirstStrToDX(s):
    return s[0].upper()+s[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(FirstStrToDX, L1))
print(L2)
#第二题：编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    return reduce(lambda x,y:x*y,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
#第三题：利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
# from functools import reduce
# def str2float(s):
# 	digits={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# 	p1=s.split('.')[0]
# 	p2=s.split('.')[1]
# 	def to_int(x,y):
# 		return x*10+y
# 	def to_list(s1):
# 		return digits[s1]
# 	p1=reduce(to_int,map(to_list,p1))
# 	p2=reduce(to_int,map(to_list,p2))
# 	s=p1+(p2(0.1**len(str(p2))))
# 	return s

# print('str2float(\'123.456\') =', str2float('123.456'))
from functools import reduce
digits= {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9 }

def str2float(s):
    p1 = s.split('.')[0]#将S分为两部分取前一部分赋值给P1作为*整数部分
    p2 = s.split('.')[1]#取后一部分赋值给P2作为*小数部分
    def to_int(x, y):
        return x*10 + y#将单一数字转化成整体数字
    def to_list(s1):
        return digits[s1]#在digits中字符对应的数字
    p1 = reduce(to_int, map(to_list, p1))#reduce（单一数字转化为整体数字）map(字符转化成相对应的数字)
    p2 = reduce(to_int, map(to_list, p2))
    s=p1+(p2*(0.1 ** len(str(p2))))#小数部分第一位乘0.1第二位乘0.1^2...
    return s

print('str2float(\'123.456\') =', str2float('123.456'))