def myfunction(nums):
  count = 0  
  for i in nums:
    if i == 1:
      count = count + 1
  return count
print(myfunction([1, 4, 6, 1, 4, 7, 4, 4]))