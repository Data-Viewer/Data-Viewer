def div_decorator(funct):
    def inner(x,y):
        if y==0:
            return "proper input"
        return funct(x,y)
    return inner
@div_decorator
def div(a,b):
    return a/b
print(div(4,0))
