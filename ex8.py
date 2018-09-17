classmates=['micheal','bob','tracy']
print(classmates)
a=len(classmates)
print(classmates[1])

#在表格末尾处插入
classmates.append('adam')
print(classmates)
#在表格任意位置插入
classmates.insert(1,'jack')
print(classmates)
#在表格末尾处删除
classmates.pop()
print(classmates)
#在表格指定位置删除
classmates.pop(1)
print(classmates)

L=[
['aple','google','microsoft'],
['java','python','ruby','php'],
['adam','bart','lisa']
]

#打印apple,python
print(L[0][0],L[1][1])
