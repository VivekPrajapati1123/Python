def myfunction(*x):
    sum = 0
    for i in x:
        sum+=i
    return sum
ans = myfunction(10,20,30)
print(ans)
