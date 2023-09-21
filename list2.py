list = [13,5,9]
n = []
x = 0
for i in list:
    for j in range(2,i):
        if i%j==0:
            n.append(1)
        else:
            n.append(0)
for j in n:
    x+=j
if x == 1:
    print("List is prime")
else:
    print("list is not prime")
