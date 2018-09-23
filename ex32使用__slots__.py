# 正常情况下，当我们定义了一个class，创建了一个class的实例后，
# 我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：
class Student(object):
	pass
#给实例绑定一个属性：
s=Student()
s.name='Micheal'
print(s.name)

#还可以尝试给实例绑定一个方法：

def set_age(self,age):# 定义一个函数作为实例方法
	self.age=age
from types import MethodType
s.set_age=MethodType(set_age,s)# 给实例绑定一个方法
s.set_age(25)# 调用实例方法
print(s.age)# 测试结果

#但是，给一个实例绑定的方法，对另一个实例是不起作用的：
s2=Student()#创建新的实例

