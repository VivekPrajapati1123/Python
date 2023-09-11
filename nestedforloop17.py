n = int(input("Enter the number:"))
for i in range(n,0,-1):
    for j in range(i):
        if j == i-1:
            print(" * ",end = "")
        else:
            print(" *  ",end = "")
    print()
