def pascals(number):
    for i in range(1,number+1):
        for j in range(number-i+1):
            print(" ",end="")
        for j in range(i):
            if j == 0 or i == 0: 
                k = 1
            else:
                k = k*(i-j)//j
            print(k,end=" ")
        print()
pascals(5)