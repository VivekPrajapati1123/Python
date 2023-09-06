n = int(input("Enter the number:"))
for i in range(n):
    for j in range(n):
        if j == n-1-i or i == j:
            print("*",end = "")
        else:
            print(" ",end = "")
    print()                                         
