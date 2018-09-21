class Animal(object):
    def run(self):
        print('Animal is running...')


# class Dog(Animal):
#     pass

# class Cat(Animal):
#     pass


# dog = Dog()
# dog.run()

# cat = Cat()
# cat.run()


class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

dog = Dog()
dog.run()
dog.eat()

class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')


dog = Dog()
dog.run()

cat = Cat()
cat.run()



#当子类和父类都存在相同的run()方法时，
#我们说，子类的run()覆盖了父类的run()，
#在代码运行的时候，总是会调用子类的run()。
#这样，我们就获得了继承的另一个好处：多态。

#要理解什么是多态，我们首先要对数据类型再作一点说明。
#当我们定义一个class的时候，我们实际上就定义了一种数据类型。
#我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样：

a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型
print(' "a" belongs to list: ',isinstance(a, list))#true
print(' "b" belongs to Animal: ',isinstance(b, Animal))#True
print(' "c" belongs to Dog: ',isinstance(c, Dog))#True

print(' "c" belongs to Animal: ',isinstance(c, Animal))#True

#看来c不仅仅是Dog，c还是Animal！
#不过仔细想想，这是有道理的，因为Dog是从Animal继承下来的，
#当我们创建了一个Dog的实例c时，我们认为c的数据类型是Dog没错，
#但c同时也是Animal也没错，Dog本来就是Animal的一种！

#所以，在继承关系中，如果一个实例的数据类型是某个子类，
#那它的数据类型也可以被看做是父类。但是，反过来就不行：

b = Animal()
print(' "b" belongs to Dog?: ',isinstance(b, Dog))

#要理解多态的好处，我们还需要再编写一个函数，
#这个函数接受一个Animal类型的变量：
def run_twice(animal):
    animal.run()
    animal.run()
    return ' '

print(run_twice(Animal()))
print(run_twice(Dog()))
print(run_twice(Cat()))

#看上去没啥意思，但是仔细想想，现在，
#如果我们再定义一个Tortoise类型，也从Animal派生：
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
print(run_twice(Tortoise()))
#你会发现，新增一个Animal的子类，不必对run_twice()做任何修改，实际上，
#任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，
#原因就在于多态。


#静态语言 vs 动态语言
#对于静态语言（例如Java）来说，如果需要传入Animal类型，
#则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。

#对于Python这样的动态语言来说，则不一定需要传入Animal类型。
#我们只需要保证传入的对象有一个run()方法就可以了：
class Timer(object):
    def run(self):
        print('Start...')

print(run_twice(Timer()))