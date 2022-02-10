def sample(str1,str2):
    return len(set(str1)&set(str2))
print(sample("hello","python"))