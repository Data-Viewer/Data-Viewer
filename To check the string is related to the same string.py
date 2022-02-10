def sample(x):
    return x in (x+x)[1:-1]
print(sample("Hi"))
print(("Hi"+"Hi")[1:-1])
x = "HiHi"
print(x[1:-1])