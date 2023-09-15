n = int(input("Enter the number:"))
i = 1
while i < 2*n:
    j = 1
    while j < 2*n:
        if i == n or j == n:
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    print()
    i+=1
        
