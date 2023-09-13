k = 65
for i in range(1,6):
    for j in range(i):
        if j%2==0:
            print(chr(k+32),end=" ")
            k+=1
        else:
            print(chr(k),end=" ")
            k+=1
    print()
    
