def myfunction1(n):
    ans = []
    for i in range(10**(n-1),10**n):
        if str(i)[0] == '2' or str(i)[-1] == '2':
            ans.append(i)
    return ans
n = int(input("Enter the number:"))
print(n)
print(myfunction1(n))