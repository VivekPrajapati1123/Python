basic = int(input("Enter the employee salary:"))

if (basic <= 5000):
    hra = basic * 0.8
    da = basic * 0.2
elif (basic <= 10000):
    hra = basic * 0.12
    da = basic * 0.30
elif (basic <= 15000):
    hra = basic * 0.15
    da = basic * 0.40
else:
    hra = basic * 0.20
    da = basic * 0.50
gross = basic + hra + da
print("Your Gross Salary",gross)
