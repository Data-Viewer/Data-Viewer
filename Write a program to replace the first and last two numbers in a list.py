def num(l):
    l[0],l[-1]=l[-1],l[0]
    return l
print(num([1,2,3,4,5,6,7,8,9]))