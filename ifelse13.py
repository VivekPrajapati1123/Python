x = int(input("Enter the income:"))

if (x < 2500):
    tax = 0
    print(tax)    
elif(x >2500 and x <= 5000):
    tax = (x - 2500) * 0.10
    print(tax)
elif(x > 5000 and x <= 10000):
    tax = 250 + (x - 5000) * 0.20
    print(tax)
elif(x>10000):
    tax = 250 + 1000 + (x - 10000) * 0.30
    print(tax)
    

    

