n = int(input("Enter the number:"))
i = 0
while i < n:
    j = 0
    while j < n:
        if j == n-1-i or i == j:
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    print()
    i+=1
        
