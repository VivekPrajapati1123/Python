maths = int(input("Enter the maths marks:"))
eng = int(input("Enter the eng marks:"))
sci = int(input("Enter the sci marks:"))

total = maths + eng +sci
print(total)

per = (total*100)/300
print(per)

if(per > 75):
    print("Grade A")
elif(per > 60 and per < 75):
    print("Grade B")
elif(per > 45 and per < 60):
    print("Grade C")
elif(per > 35 and per < 45):
    print("Grade D")
else:
    print("Student is fail")
