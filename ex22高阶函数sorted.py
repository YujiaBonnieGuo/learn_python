#排序也是在程序中经常用到的算法。
#无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小
#Python内置的sorted()函数就可以对list进行排序：
print(sorted([36,5,-12,9,-21]))
#此外，sorted()函数也是一个高阶函数，
#它还可以接收一个key函数来实现自定义的排序，例如
#按绝对值大小排序
key=sorted([36,5,-12,9,-21],key=abs)
print('按照绝对值排序',key)
#按照字母序排序
key=sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower)
print('正向不分大小写排序：', key)
#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
key=sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print('反向不分大小写排序：',key)
#假设我们用一组tuple表示学生名字和成绩：
#请用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def byname(T):
    return T[0]

def byscore(t):
    return t[1]

L2 = sorted(L, key=byname)
L3 = sorted(L, key=byscore,reverse=True)
print(L2)
print(L3)