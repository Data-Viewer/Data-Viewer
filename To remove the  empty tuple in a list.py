def fun(sample):
    sample = [s for s in sample if s]
    return sample
sample =[(),('ram',3,4),(),('raj','krish','jan')]
print(fun(sample))