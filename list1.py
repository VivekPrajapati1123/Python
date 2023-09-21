list = [1,3,2,10,4,5,8,6,9,7]
n = len(list)
for i in range(n):
    for j in range(i+1,n):
        if list[i] > list[j]:
            list[i],list[j] = list[j],list[i]
print(list)
