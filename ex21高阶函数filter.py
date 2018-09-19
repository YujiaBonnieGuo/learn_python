#和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，
#filter()把传入的函数依次作用于每个元素，
#然后根据返回值是True还是False决定保留还是丢弃该元素

#删掉偶数，只保留奇数
def is_odd(n):
	return n%2==1
print(list(filter(is_odd,[1,2,3,4,5,6,9,10,15])))
#删掉空字符串
def not_empty(s):
	return s and s.strip()
	#s.strip(rm):删除s字符串中开头、结尾处，位于 rm删除序列的字符,
	#当rm为空时，默认删除空白符（包括'\n', '\r',  '\t',  ' ')
	#s.lstrip(rm)： 删除s字符串中开头处，位于 rm删除序列的字符
	#s.rstrip(rm)： 删除s字符串中结尾处，位于 rm删除序列的字符
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
#用filter求素数
#1.构造一个从3开始的奇数序列：
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# p=_odd_iter()
# n=0
# while True:
# 	print(next(p))
# 	n+=1
# 	if n>20:
# 		break

#2.定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0#从n中选取一个数字为x，用x整除n中所有数
                              #取余数，若余数大于零（即没有数可以被整除）
                              #则保留X 否则丢弃（即丢弃掉可以被整除的数）





#3.定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印100以内的素数:
for n in primes():
    if n < 20:
        print(n)
    else:
        break

#回数是指从左向右读和从右向左读都是一样的数，
#例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    l = list(str(n))
    return l[::-1] == l[:]

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))