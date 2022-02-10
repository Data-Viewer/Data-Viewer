def fun(test):
    del test['d']
    return test
print(fun({'s':3, 'd':5, 'a':7} ))