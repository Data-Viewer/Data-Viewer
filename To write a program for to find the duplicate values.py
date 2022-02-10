sample = [1,2,3,4,5,6,6,6]
duplicate_dict={}
for i in sample:
    duplicate_dict[i]=sample.count(i)
print(duplicate_dict)