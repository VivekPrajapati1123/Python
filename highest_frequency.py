def myfunction1(n):
    dict = {}
    for i in n:
        if i in dict:
            dict[i]+=1
        else:
            dict[i] = 1
    ans = sorted(dict.items(),key = lambda x:x[1],reverse = True)
    return ans 
list1 = [2,3,8,4,7,8,9,4,2,4,9,5,6,1,7,2]
ans = myfunction1(list1)
print(ans)


