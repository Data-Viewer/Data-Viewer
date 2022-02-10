def fun(x):
    for i in x:
        z = i**3
        if z % 2 ==0:
            print(z)
fun((1,2,3,4,5,6,7))