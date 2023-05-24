# https://docs.python.org/2/library/datetime.html
from datetime import datetime, timedelta


d1 = datetime.strptime('21/12/1996 10:10:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('21/12/2020 10:10:00', '%d/%m/%Y %H:%M:%S')
dif = d2 - d1
print(dif.)


