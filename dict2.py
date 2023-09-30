
dict1 = {1:34,2:56,3:45,4:89,5:65}
x = dict1.values()
list1 = list(x)
list1 = sorted(list1)
min = list1[0]
max = list1[len(list1)-1]
print(min)
print(max)



dict1 = {1:34,2:56,3:45,4:89,5:65}
x = dict1.values()
list1 = list(x)
#print(list1)
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] < list1[j]:
            list1[i],list1[j] = list1[j],list1[i]
#print(list1)




