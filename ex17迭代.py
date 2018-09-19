#iteration
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print(key)

#如果要迭代value
for k,v in d.items():
	print(k,v)

#判断是否可迭代
from collections import Iterable
print('str是否可迭代')
print(isinstance('abc', Iterable)) # str是否可迭代
print('list是否可迭代')
print(isinstance([1,2,3], Iterable)) # list是否可迭代
print('整数是否可迭代')
print(isinstance(123, Iterable))# 整数是否可迭代

#下标循环:enumerate
for i,value in enumerate(['A','B','C']):
	print(i,value)

#使用迭代查找一个list中最小和最大值，并返回一个tuple
def find_min_and_max(l):
	min=l[0]
	max=l[0]
	for i in l:
		if i<=min:
			min=i
		elif i>=max:
			max=i;
	return(min,max)

print(find_min_and_max([5,6,8,7,2,6]))