n = int(input("Enter the number:"))
a,b = 0,1
c = 0
while c < n:
    print(a)
    c = a + b
    a = b
    b = c
    c+=1
