
class Val(object):
    __slots__ = ['value']
    def __init__(self,value= 0):
        self.value = value

v = Val(1)
print(v)