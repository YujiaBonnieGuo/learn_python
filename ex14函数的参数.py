#二次方
def power(x):
	return x*x

print(power(5))

#n次方
def power2(x,n):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s

print(power2(3,3))

#一年级小学生注册的函数
def enroll(name,gender,age=6,city='beijing'):
	print('name:',name)
	print('gender:',gender)
	print('age:',age)
	print('city:',city)

print(enroll('sarah','f'))

#先定义一个函数，传入一个list，添加一个END再返回
def add_end(l=[]):
	l.append('end')
	return l

print(add_end([1,2,3]))
print(add_end(['x','y','z']))
print(add_end())
print(add_end())

#改进后的end

def add_end(l=None):
	if l is None:
		l=[]
	l.append('end')
	return l

print(add_end([1,2,3]))
print(add_end(['x','y','z']))
print(add_end())
print(add_end())

#我们以数学题为例子，给定一组数字a，b，c……，请计算a^2 + b^2 + c^2 + ……
def calc(numbers):
	sum=0
	for n in numbers:
		sum=sum+n**2
	return sum

print(calc([1,2,3]))
print(calc([1,3,5,7]))
#修改为可变参数
def calc(*numbers):  #*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
	sum=0
	for n in numbers:
		sum=sum+n**2
	return sum

print(calc(1,2,3))
print(calc(1,3,5,7))

#关键字参数kw
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

print(person('michael',30))
print(person('Adam', 45, gender='M', job='Engineer'))
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 24, **extra))
#限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数
def person(name,age,*,city,job):#如果没有可变参数，就必须加一个*作为特殊分隔符
    print(name,age,city,job)

person('Jack', 24, city='Beijing', job='Engineer')

#参数组合
#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

print(f1(1, 2))
print(f1(1, 2, c=3))
print(f1(1, 2, 3, 'a', 'b'))
print(f1(1, 2, 3, 'a', 'b', x=99))

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
print(f2(1, 2, d=99, ext=None))

#以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def product(*numbers):
	if len(numbers)==0:
		raise TypeError('参数不能为空')
	else:
	    a=1
	    for n in numbers:
		    a=a*n
	return a

print(product(5,6,7,9))