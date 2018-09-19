#generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，
#直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
#使用循环调用generator因为generator是可迭代对象
g = (x * x for x in range(10))
for n in g:
	print(n)

#Fibonacci数列
def fib(max):
	n,a,b=0,0,1
	while n<max:
		print(b)
		a,b=b,a+b#t = (b, a + b) # t是一个tuple a = t[0] b = t[1]
		n=n+1
	return 'done'

max=int(input('max number in fibonicci: '))
print(fib(max))

#要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

max=int(input('max number in fibonicci: '))
for n in fib(max):
	print(n)

#定义一个generator，依次返回数字1，3，5
def odd():
	print('step1')
	yield (1)
	print('step2')
	yield (3)
	print('step3')
	yield (5)
o=odd()
next(o)
next(o)
next(o)

#但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
#如果想要拿到返回值，必须捕获StopIteration错误，
#返回值包含在StopIteration的value中：
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break