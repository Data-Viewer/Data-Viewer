def swap(list):
    size = len(list)
    temp = list[0]
    list[0]=list[size-1]
    list[size-1]=temp
    return list
list = [12,34,55,77,99]
print(swap(list))