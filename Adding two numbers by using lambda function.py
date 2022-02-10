def funt(n):
    return lambda x:x+n
funt=lambda n: lambda x:x+n
funt =funt(1)
print(funt(3))