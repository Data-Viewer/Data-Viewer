def function():
    yield 1
    yield 2
    yield 3
for j in function():
    print(j)
