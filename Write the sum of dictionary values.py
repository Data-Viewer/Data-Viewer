def sum_text(dict):
    sum = 0
    for i in dict.values():
        sum=sum+i
    return sum
dict = {'shall':55,'anvi':33,'chandu':22}
print('sum:', sum_text(dict))