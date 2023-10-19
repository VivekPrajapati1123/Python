# def myfunction1(n):
#     if n == 1 or n == 2:
#         return [0,1]
#     else:
#         ans = myfunction1(n-1)
#         ans.append(ans[-1]+ans[-2])
#         return ans
# x = int(input("Enter the value of x:"))
# ans = myfunction1(x)
# print(ans)

myfunction1 = lambda n: [0,1]  if i==0 else [0] if i==1 else [0,1] if i==2 else myfunction1(n-2) +  myfunction1(in-1)[-1]]

x = int(input("Entre the value of x:"))
ans = myfunction1(x)
print(ans) 