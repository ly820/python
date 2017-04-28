class LazyProperty(object):
    """
    LazyProperty
    explain: http://www.spiderpy.cn/blog/5/
    """

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value

class Area(object):
    def __init__(self,r):
        self.r = r
    @LazyProperty
    def area(self):
        return self.r * self.r * 3.14




a = Area(4)
print(a.area)
print(a.__dict__['area'])
print(Area.area.__get__(a,Area))

