def add(a):
    def cash(b):
        return a+b
    return cash
run=add(15)
print(run(20))