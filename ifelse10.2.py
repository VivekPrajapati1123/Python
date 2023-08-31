a = int(input("Enter the a value:"))
b = int(input("Enter the b value:"))
c = int(input("Enter the c value:"))

if a>b:
    if a>c:
        print("a is largest number")
if b>c:
    if b>a:
        print("b is largest number")
else:
    print("c is largest number")
