for i in range(2,50):
    k=0
    for j in range(2,i-1):
        if i%j==0:
            k+=1
    if k==0:
        print(i)