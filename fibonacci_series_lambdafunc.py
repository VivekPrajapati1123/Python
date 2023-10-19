myfunction1 = lambda n : [0,1] if n == 1 else [0,1] if n == 2 else myfunction1(n-1)+[myfunction1(n-1)[-1]+myfunction1(n-1)[-2]]

x = int(input("Enter the value of x:"))
ans = myfunction1(x)
print(ans)