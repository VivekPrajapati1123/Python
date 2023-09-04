unit = int(input("Enter the unit:"))

if (unit <= 100):
    bill = unit*0.6
elif (unit > 100 and unit <= 300):
    b1 = 0.6*100
    b2 = (unit-100)*0.8
    totalbill = b1 + b2
    print(totalbill)
else:
    b1 = 0.6*100
    b2 = 0.8*200
    b3 = (unit - 300)*0.9
    totalbill = b1 + b2 + b3
    print(f"{totalbill}")
if totalbill < 50:
    finalbill = 50
elif totalbill > 300:
    finalbill = totalbill + (totalbill * 0.15)
else:
    finalbill = totalbill
print("Your Final Bill Amount",finalbill)
    
