def sample(list):
    return[i for i in list if list.count(i)==1]
print(sample([1,2,3,3,4,5,6,6,6,8,9]))