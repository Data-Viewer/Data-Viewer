def sample(x):
    return (lambda y:x+y)
s=sample(4)
print(s(8))
t=sample(7)
print(t(8))