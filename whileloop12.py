n = int(input("Enter the number:"))
i = 0
while i <= n:
    j = 0
    while j <= n-i-1:
        print("   ",end=" ")
        j+=1
    j = 0
    while j <= n:
        if i == 0 or i == n or j == 0 or j == n:
            print(" * ",end=" ")
        else:
            print("   ",end=" ")
        j+=1
    print()
    i+=1
