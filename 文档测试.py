# 如果你经常阅读Python的官方文档，可以看到很多文档都有示例代码。比如re模块就带了很多示例代码：
import re
m=re.search('(?<=abc)def','abcdef')
print(m.group())
# 可以把这些示例代码在Python的交互式环境下输入并执行，结果与文档中的示例代码显示的一致。

# 这些代码与其他说明可以写在注释中，然后，由一些工具来自动生成文档。既然这些代码本身就可以粘贴出来直接运行，那么，可不可以自动执行写在注释中的这些代码呢？

# 答案是肯定的。

# 当我们编写注释时，如果写上这样的注释：
def abs(n):
    '''
    Function to get absolute value of number.
    example"
    >>>abs(1)
    1
    >>>abs(-1)
    1
    '''
    return n  if n>=0 else (-n)


