set1 = {20,30,35,12,45}
set2 = {1,2,45,5,10,20}
set3 = set()
for i in set1:
    if i in set2:
        set3.add(i)
print(set3)
'''
set1 = {20,30,35,12,45}
set2 = {1,2,45,5,10,20}
set3 = set()
for i in set1:
    for j in set2:
        if i == j:
            set3.add(j)
print(set3)


set1 = {20,30,35,12,45}
set2 = {1,2,45,5,10,20}
print(set1&set2)
'''





