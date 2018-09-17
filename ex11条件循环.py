names=['micheal','bob','tracy']
for name in names:
	print(name)
#for x in[]结构
sum=0
for x in[1,2,3,4,5,6,7,8,9,10]:
	sum=sum+x
print(sum)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

#while结构
sum=0
n=99
while n>0:
	sum=sum+n
	n=n-2
print(sum)

names=['micheal','bob','tracy']
for name in names:
    print('hello',name,'!')

#在循环中，break语句可以提前退出循环。例如，本来要循环打印1～100的数字：
n=1
while n<=100:
	if n>10: # 当n = 11时，条件满足，执行break语句
	    break# break语句会结束当前循环
	print(n)
	n=n+1
print('END')
#c如果我们想只打印奇数，可以用continue语句跳过某些循环：

# n=0
# while n<10:
#     n=n+1
#     if n%2==0: # 如果n是偶数，执行continue语句
#         continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
#     print(n)




a=0
while a<10:
    a=a+1
    if a%2==0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print('a=',a)


#有些时候，如果代码写得有问题，会让程序陷入“死循环”，也就是永远循环下去。
#这时可以用Ctrl+C退出程序，或者强制结束Python进程。
