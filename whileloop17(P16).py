n = int(input("Enter the number:"))
i = 0
while i < n:
    j = 0
    while j < n-i:
         print(" ",end=" ")
         j+=1
    
    j = 0
    while j < i+1:
        print(" * ",end=" ")
        j+=1
    print()
    i+=1
