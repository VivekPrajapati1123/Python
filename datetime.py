import datetime
print(datetime.datetime.now())

from datetime import date
print(date.today())

from datetime import date
x = date.today()
print(str(x.day) + str(x.month) + str(x.year))

from datetime import date
x = date(2023,10,24)
print(x)
