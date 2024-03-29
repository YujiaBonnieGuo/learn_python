def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)

print(fact(1))
print(fact(5))

#解决递归调用栈溢出的方法是通过尾递归优化
# def fact(n):
#     return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact_iter(5, 1))

#汉诺塔的移动可以用递归函数非常简单地实现
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

print(move(3, 'A', 'B', 'C'))
