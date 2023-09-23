list1 = [99,133,132,132,133,99]
n = len(list1)
reversed_list = [list1[i] for i in range(n-1,-1,-1)]
if list1 == reversed_list:
    print("list is palidrome")
else:
    print("list is not palidrome")
