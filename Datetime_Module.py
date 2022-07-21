import datetime

mytime = datetime.time(2,20)

print(mytime.minute)
print(mytime.hour)
print(mytime)

# PAra explorar date objects
today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)

# Ahora para unir tiempo y hora
from datetime import datetime
mydatetime = datetime(2021,10,3,14,20,1)
print(mydatetime)

# PAra hacer un reemplazo
mydatetime = mydatetime.replace(year=2020)
print(mydatetime)

# Date
from datetime import date
date1 = date(2021,11,3)
date2 = date(2020,11,3)
d = date1 - date2
print(d.days)

# Datetime
datetime1 = datetime(2021,11,3,22,0)
datetime2 = datetime(2020,11,3,12,0)

d = datetime1 - datetime2
print(d.total_seconds())




