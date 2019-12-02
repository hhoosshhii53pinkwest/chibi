import pegpy
#from pegpy.tpeg import ParseTree
peg = pegpy.grammar('chibi.tpeg')
parser = pegpy.generate(peg)
'''
tree = parser('1+2*3')
print(repr(tree))
tree = parser('1@2*3')
print(repr(tree))
'''
class Expr(object):
    @classmethod
    def new(cls, v):
        if isinstance(v, Expr):
            return v
        return Val(v)
class Val(Expr):
    __slots__ = ['value']
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f'Val({self.value})'
    def eval(self, env: dict):
        return self.value
e = Val(0)
assert e.eval({}) == 0
class Binary(Expr):
    __slots__ = ['left', 'right']
    def __init__(self, left, right):
        self.left = Expr.new(left)
        self.right = Expr.new(right)
    def __repr__(self):
        classname = self.__class__.__name__
        return f'{classname}({self.left},{self.right})'
class Add(Binary):
    __slots__ = ['left', 'right']
    def eval(self, env: dict):
        return self.left.eval(env) + self.right.eval(env)
class Sub(Binary):
    __slots__ = ['left', 'right']
    def eval(self, env: dict):
        return self.left.eval(env) - self.right.eval(env)
class Mul(Binary):
    __slots__ = ['left', 'right']
    def eval(self, env: dict):
        return self.left.eval(env) * self.right.eval(env)
class Div(Binary):
    __slots__ = ['left', 'right']
    def eval(self, env: dict):
        return self.left.eval(env) // self.right.eval(env)
class Mod(Binary):
    __slots__ = ['left', 'right']
    def eval(self, env: dict):
        return self.left.eval(env) % self.right.eval(env)

class Var(Expr):
    __slots__ = ['name']
    def __init__(self,name):
        self.name = name
    def eval(self,env: dict):
        if self.name in env:
            return env[self.name]
        raise NameError(self.name)

class Assign(Expr):
    __slots__ = []
    


print('少しテスト')

env = {}
e = Assign('x',Val(1)) # x = 1
print(e.eval(env)) #1
e = Assign('x',Add(Var('x'),Val(2))) #x = x + 2
print(e.eval(env)) #3


promt('テスト終わり')

def conv(tree):
    if tree == 'Block':
        return conv(tree[0])
    if tree == 'Val' or tree == 'Int':
        return Val(int(str(tree)))
    if tree == 'Add':
        return Add(conv(tree[0]), conv(tree[1]))
    if tree == 'Sub':
        return Add(conv(tree[0]), conv(tree[1]))
    if tree == 'Mul':
        return Add(conv(tree[0]), conv(tree[1]))
    if tree == 'Div':
        return Add(conv(tree[0]), conv(tree[1]))
    if tree == 'Mod':
        return Add(conv(tree[0]), conv(tree[1]))
    print('@TODO', tree.tag)
    return Val(str(tree))
def run(src: str):
    tree = parser(src)
    if tree.isError():
        print(repr(tree))
    else:
        e = conv(tree)
        print(repr(e))
        print(e.eval({}))
def main():
    try:
        while True:
            s = input('>>> ')
            if s == '':
                break
            run(s)
    except EOFError:
        return
if __name__ == '__main__':
    main()