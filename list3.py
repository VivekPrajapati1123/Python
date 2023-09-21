list = [9,9,6,6,5,7,7,5,5,2,2,1,1,3,3]
n = len(list)
i=0
while i < len(list)-1:
    if list[i]==list[i+1]:
        list.pop(i)
    i+=1
print(list)
        
                                                         
