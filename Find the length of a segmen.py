def sample(num1,num2):
    [x1,y1],[x2,y2]=num1,num2
    return round(((x1-x2)**2 + (y1-y2)**2)**0.5,2)

print(sample([1,2],[2,3]))