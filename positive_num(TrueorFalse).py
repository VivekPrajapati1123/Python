def myfunction1(lst,n):
    if n <= 0:
        return False
    a = len(lst)
    if a%n == 0:
        return True
    else:
        return False
list1 = [1,2,3,4,5,6,7,8,9,10]
break_num = 4
ans = myfunction1(list1,break_num)
print(list1)
print(break_num)
print(ans)