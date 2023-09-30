list1 = [1,2,3,4,5]
copy_list = list1
print(copy_list)
import copy
list2 = copy.copy(list1)
print(list2)
list3 = []
list3.extend(list1)
print(list3)