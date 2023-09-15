n = int(input("Enter the number:"))
i = 0
while i < n:
    j = 0
    while j < i+1:
        print("*",end="")
        j+=1
    print()
    i+=1
i = n-2
while i > 0:
    j = 0
    while j < i+1:
        print("*",end="")
        j+=1
    print()
    i-=1
