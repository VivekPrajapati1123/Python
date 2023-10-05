def myfunction1(n):
    s = 1
    for i in range(1,n+1):
        s*=i
    return s
x = 4
s = myfunction1(x)
print(s)

        