# coding:utf-8

class Foo(object):
    """类三种方法语法形式"""

    def instance_method(self):
        print("是类{}的实例方法，只能被实例对象调用".format(Foo))

    @staticmethod
    def static_method():
        print("是静态方法")

    @classmethod
    def class_method(cls):
        print("是类方法")

foo = Foo()
foo.instance_method()
foo.static_method()
foo.class_method()
print('----------------')
Foo.static_method()
Foo.class_method()

# 1. 实例方法只能由实例对象调用
# 2.静态方法, 类方法, 可以由实力对象和类调用
# 3. 实例方法第一个参数必须要传实例对象,通常是 self
# 4. 静态方法参数没有要求
# 5. 类方法法第一个参数默认要传类, 一般习惯用 cls


# 类方法,由 @classmethod 修饰的方法,
class Book(object):

    def __init__(self, title):
        self.title = title

    @classmethod
    def create(cls, title):
        book = cls(title=title)
        return book

book1 = Book("python")
book2 = Book.create("python and django")
print(book1.title)
print(book2.title)

# 静态方法,由 @staticmethod 修饰的方法

class Foo(object):
    X = 1
    Y = 2

    @staticmethod
    def averag(*mixes):
        return sum(mixes) / len(mixes)

    @staticmethod
    def static_method():
        return Foo.averag(Foo.X, Foo.Y)

    @classmethod
    def class_method(cls):
        return cls.averag(cls.X,cls.Y)
        # return cls.static_method()

# foo = Foo()
# print(foo.static_method())
# print(foo.class_method())

# 继承中的区别
class Foo(object):
    X = 1
    Y = 2

    @staticmethod
    def averag(*mixes):
        return sum(mixes) / len(mixes)

    @staticmethod
    def static_method():
        return Foo.averag(Foo.X, Foo.Y)

    @classmethod
    def class_method(cls):
        return cls.averag(cls.X, cls.Y)

print(Foo.static_method())  # 1.5
print(Foo.class_method())   # 1.5

class Son(Foo):
    X = 3
    Y = 5

    @staticmethod
    def averag(*mixes):
        return sum(mixes) / 3

p = Son()
print(p.static_method())    # 1.5
print(p.class_method())     # 2.6666666666666665
print(Son.static_method())  # 1.5
print(Son.class_method())   # 2.6666666666666665

"""
(1) Son 继承了 Foo, Son类继承了Foo类的静态方法,子类(Son)调用该方法,调用的是父类(Foo)的方法和父类的类属性（X = 1, Y = 2）
(2) Son 继承了 Foo, Son类集成了Foo类的类方法,子类(Son)调用该方法,调用的是子类(Son)的方法和子类的类属性(X = 3, Y = 5)
(3) p是Son的实例,p继承了了Foo的静态方法,p调用该方法,调用的是父类(Foo)的方法和父类的类属性(X = 1, Y = 2)
(4) p是Son的实例,p继承了Foo的类方法,p调用该方法,调用的是子(Son)类的方法和子类的类属性(X = 3, Y = 5)
"""

# 总结：
#    对于静态方法,子类和子类实例都继承,子类和子类势力调用继承的静态方法时,调用的是父类的方法和父类的类属性,结果和父类调用结果一样
#    对于类方法,子类和子类实例也都继承,子类和子类实例调用继承的类方法时,调用的是子类和子类实例本身的方法和类属性