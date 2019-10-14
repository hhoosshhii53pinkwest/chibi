class Expr(object):
    pass
class Val(Expr):
    __slots__ = ['value']
    def __init__(self,value= 0):
        self.value = value
    def __repr__(self):
        return f'Val({self.value})'
    def eval(self):
        return self.value

v = Val(1)
print(v)
assert v.eval() == 1

assert isinstance(v, Expr) #==>True
assert isinstance(v, Val) #==>True
assert not isinstance(v, int) 

def toExpr(a):
    if not isinstance(a, Expr):
        a = Val(a)
    return a


class Add(Expr):
    __slots__=['left','right']
    def __init__(self, a, b):
        if not isinstance(a, Expr):
            a = Val(a)
        if not isinstance(b, Expr):
            b = Val(b)   
        self.left = a
        self.right = b
    def eval(self):
        return self.left.eval() + self.right.eval()

    e = Add(1,Add(1,2))
    print(e.eval())
    assert e.eval() == 4

e = Add(Val(1),Add(Val(2),Val(3))) #1+2+3 ==> 6
assert e.eval() == 6

print()

class Mul(Expr):
    __slots__=['left','right']
    def __init__(self, a, b):
        self.left = a #aとbは式
        self.right = b
    def eval(self):
        return self.left.eval() * self.right.eval()


e = Mul(Val(1), Val(2)) #1*2
print(e.eval())
assert e.eval() == 2

print()

class Sub(Expr):
    __slots__=['left','right']
    def __init__(self, a, b):
        self.left = a
        self.right = b
    def eval(self):
        return self.left.eval() - self.right.eval()

        
e = Sub(Val(1), Val(2)) #1*2
print(e.eval())
assert e.eval() == -1

print()

class Div(Expr):
    __slots__=['left','right']
    def __init__(self, a, b):
        self.left = a
        self.right = b
    def eval(self):
        return self.left.eval() // self.right.eval()

        
e = Div(Val(7), Val(2)) #1*2
print(e.eval())
assert e.eval() == 3

print()

