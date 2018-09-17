#取前n个元素
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)

#切片
print(L[0:3])#L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3
print(L[:3])#如果第一个索引是0，还可以省略

#1-100的数列前10个数，每两个取一个
L = list(range(100))
print(L[:10:2])
#所有数，每5个取一个：
print(L[::5])
#字符串'xxx'也可以看成是一种list，每个元素就是一个字符
print('ABCDEFG'[:3])

#实现一个trim()函数，去除字符串首尾的空格
def trim(s):
    while s[:1]==' ':
        s=s[1:]
    while s[-1:]==' ':
        s=s[:-1]
    return s

print(trim(' abc  a123  3'))
print(trim('     abc    a123    3    '))#只能是字符串的首位，没有办法监测到每一个字符段
