k = 1
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print( k ,end="")
        if k == 0:
            k=1
        else:
            k = 0
        j+=1
    print()
    i+=1
