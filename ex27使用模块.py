#我们以内建的sys模块为例，编写一个hello的模块：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test module'#字符串，表示模块的文档注释，
#任何模块代码的第一个字符串都被视为模块的文档注释
__author__='Micheal Liao'

import sys

def test():
	args=sys.argv
	if len(args)==1:
		print('Hello,world!')
	elif len(args)==2:
		print('Hello,%s!'%args[1])
	else:
		print('too many arugments!')

	if __name__=='__main__':
		test()

#print('调用sys模块执行的结果是：',sys.argv(test('Micheal')))

def _private1_(name):
	return 'hello,%s'%name
def _private2_(name):
	return'hi,%s'%name

# ' a test module '
# import ex27使用模块
def greeting(name):
	if len(name)>3:
		return _private1_(name)
	else:
		return _private2_(name)

print(greeting('Micheal'))
print(greeting('May'))
