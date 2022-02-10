def my_funt(x):
    return list(dict.fromkeys(x))
mylist = my_funt(["a","b","c","c"])
print(mylist)