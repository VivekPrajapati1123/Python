list1 = [1,2,3,4,5,6,7,8,9,10]
n = int(input("Enter the number:"))
step = len(list1)//n
splitted = [list1[i::step] for i in range(step)]
#splitted = [list1[i:i+2:1] for i in range(step)]
print(splitted)