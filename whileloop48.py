k = 65
i = 0
while i < 6:
    j = 0
    while j < i:
        if j%2==0:
            print(chr(k+32) ,end=" ")
            k+=1
        else:
            print(chr(k) ,end=" ")
            k+=1
        j+=1
    print()
    i+=1
