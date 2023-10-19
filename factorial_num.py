def myfunction1(n):
    s = 1
    for i in range(1,n+1):
        s*=i
    return s
x = int(input("Entre the value of x:"))
s = myfunction1(x)
print(s)

        