def myfunction1(num,add):
    ans = [add]*(2*len(num)-1)
    ans[::2] = num
    return ans
num = [1,2,3,4,5,6,7,8,9,10]
add = 90
print(num)
print(add)
print(myfunction1(num,add))