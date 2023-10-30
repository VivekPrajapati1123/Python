#import datetime
import calendar
def myfunction(s_year,s_month):
    if s_month > 1:
        e_year = s_year + 1
    else:
        e_year = s_year
    e_month = s_month - 1
    
    while s_year <= e_year and s_month <= 12:
        c = calendar.TextCalendar(calendar.MONDAY)
        print(c.formatmonth(s_year,s_month))
        s_month+=1
    s_year+=1
    s_month=1
    while s_month <= e_month:
        c = calendar.TextCalendar(calendar.MONDAY)
        print(c.formatmonth(s_year,s_month))
        s_month+=1
#print(myfunction(2024,4 ))
s_year = int(input("Enter the year:"))
s_month = int(input("Enter the month:"))
ans = myfunction(s_year,s_month)
print(ans)


'''
#import datetime
import calendar
def myfunction(s_year,s_month):
    if s_month > 1:
        e_year = s_year + 1
    else:
        e_year = s_year
    e_month = s_month - 1
    
    for i in range(1,13):
        print(calendar.month(s_year,s_month))
        s_month+=1
    s_year+=1
    s_month=1
    for j in range():
        print(calendar.prcal(s_year,s_month,2,3,5,6))
        s_month+=1
#print(myfunction(2024,4 ))
s_year = int(input("Enter the year:"))
s_month = int(input("Enter the month:"))
ans = myfunction(s_year,s_month)
print(ans)



'''




