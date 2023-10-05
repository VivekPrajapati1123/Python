def myfunction(x):
    sum = 0
    for i in x:
        sum+=i
    return sum
tuple1 = (1,2,3,4,5,6,7,8,9,10)
list1 = [11,12,13,14,15,16,17,18,19,20]
set1 = {21,22,23,24,25,26,27,28,29,30}
ans1 = myfunction(tuple1)
ans2 = myfunction(list1)
ans3 = myfunction(set1)
print(ans1)
print(ans2)
print(ans3)