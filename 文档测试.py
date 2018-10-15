# 如果你经常阅读Python的官方文档，可以看到很多文档都有示例代码。比如re模块就带了很多示例代码：
import re
m=re.search('(?<=abc)def','abcdef')
print(m.group())
