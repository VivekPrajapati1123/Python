list1 = [[1,1],[2,2],[3,3],[4,4]]
n = len(list1)
i = 0
for i in range(n):
   if list1[i][0] == list1[i][1]:
        list1[i].pop(0)
print(list1)


