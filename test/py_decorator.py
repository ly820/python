
# 1. 函数是对象可以赋值给变量
def greet(name):
    return "hello " + name

greet_someone = greet
# print(greet_someone("John"))
# Outputs: hello John


# 2. 一个函数可以在另一个函数内部定义,运行

def greet(name):
    def get_message():
        return "Hello "
    result = get_message() + name
    return result

# print(greet("John"))
# Outputs: Hello John

# 3. 一个函数对象可以作为参数传递到另一个函数中去

# def greet(name):
#     return "Hello " + name

def call_func(func):
    other_name = "John"
    return func(other_name)

# print(call_func(greet))
# Outputs: Hello John

# 4. 函数可以嵌套一个函数返回它内部的另一个函数

# 不带参数
# def compose_greet_func():
#     def get_message():
#         return "Hello there!"
#     return get_message

#greet = compose_greet_func()
# print(greet())
# Outputs: Hello there!

# 带参数
def compose_greet_func(name):
    def get_message():
        return "Hello there " +name+ "!"
    return get_message

# greet = compose_greet_func("John")
# print(greet())
# Outputs: Hello there John!

# 装饰器的原理

def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)

def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper

get_text = p_decorate(get_text)
# print(get_text("John"))
# Outputs: <p>lorem ipsum, John dolor sit amet</p>

@p_decorate
def get_text(name):
    return "lorem imsum, {0} dolor sit amet".format(name)

#print(get_text("John"))
# Outputs: <p>lorem imsum, John dolor sit amet</p>

# 上面两个输出结果相同。

# 更多例子


def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper

def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper

#get_text = div_decorate(p_decorate(strong_decorate(get_text)))
@div_decorate
@p_decorate
@strong_decorate
def get_text(name):
    return "lorem imsum, {0} dolor sit amet".format(name)

# print(get_text("John"))
# Outputs: <div><p><strong>lorem imsum, John dolor sit amet</strong></p></div>

# 装饰器不光可以修饰函数,还可以修饰方法
# 装饰器不光可以是函数,还可以是类

# 修饰方法

# def p_decorate(func):
#     # 注意该装饰器修饰的是方法,方法至少有一个参数self,所以该函数也必须有个参数,为了自己明白,用self比较合适
#     def func_wrapper(self):
#         return "<p>{0}</p>".format(func(self))
#     return func_wrapper
#
# class Person(object):
#     def __init__(self):
#         self.name = "John"
#         self.family = "Doe"
#
#     @p_decorate
#     def get_fullname(self):
#         return self.name + " " + self.family
#
# my_person = Person()
# print(my_person.get_fullname())
# Outputs: <p>John Doe</p>

# 装饰器装饰的方法可能不止一个参数,为了更加的保险可以像下面这样
def p_decorate(func):
   def func_wrapper(*args, **kwargs):
       return "<p>{0}</p>".format(func(*args, **kwargs))
   return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name+" "+self.family
# my_person = Person()
# print(my_person.get_fullname())

# 我们也可以传递参数到装饰器中
# 上面三个装饰器(div_decorate,p_decorate,strong_decorate)
# 虽然包装的标签不一样,但是功能是一样的。我们可以用一个更一般的方式实现用样的功能


def tags(tag_name):
    """hei"""
    def tags_decorator(func):
        """ddd"""
        def func_decorator(name):
            """lala"""
            return "<{0}>{1}<{0}>".format(tag_name,func(name))
        return func_decorator
    return tags_decorator


@tags("p")
def get_text(name):
    """haha"""
    return "Hello " + name

# print(get_text("John"))
# Outputs: <p>John Doe</p>

# 装饰器只是修改函数的功能,不能保持最初函数的__name__,__doc__,__module__属性
# 最初函数的__name__,__doc__,__moudle__这些属性，被装饰器函数覆盖了
print(get_text.__name__)
print(get_text.__doc__)
print(get_text.__module__)


# 上面的问题可以 functools 模块中的 wraps 解决
# wraps 是一个装饰器
from functools import wraps
def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

@tags("p")
def get_text(name):
    """returns some text"""
    return "Hello "+name

print(get_text.__name__)
print(get_text.__doc__)
print(get_text.__module__)


class myDecorator(object):

    def __init__(self, f):
        print("inside myDecorator.__init__()")
        f() # Prove that function definition has completed

    def __call__(self):
        print("inside myDecorator.__call__()")


@myDecorator
def aFunction():
    print("inside aFunction()")

print("Finished decorating aFunction()")

aFunction()