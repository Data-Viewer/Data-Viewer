def my_generator():
    print('first item')
    yield 1
    
    print('second item')
    yield 2
    
    print('third item')
    yield 3
    
for i in my_generator():
    print(i)
