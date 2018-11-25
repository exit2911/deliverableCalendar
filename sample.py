from pandas.tseries.offsets import BMonthEnd
from datetime import date

d=date.today()

offset = BMonthEnd()

#Last day of current month
offset.rollforward(d)

#Last day of previous month
offset.rollback(d)



#-----
from pandas.tseries.offsets import BMonthEnd
from datetime import date
import datetime
import pandas as pd
from pandas.tseries.offsets import BDay
import numpy as np
import holidays
from bdateutil import relativedelta

d=date.today()

offset = BMonthEnd()

#Last day of current month
c = offset.rollforward(d)
np.busday_offset('2018-11-09',1)
#Last day of previous month
offset.rollback(c) + BDay(10)

a = offset.rollforward(c) + BDay(10)

off = ['2019-01-01','2019-01-21','2019-02-18','2019-05-27','2019-07-04','2019-09-02','2019-10-12','2019-11-11','2019-11-28','2019-12-25']

for i in off:
    a = np.is_busday(i)
    
    print(a)


date(2018, 11, 11) + relativedelta(bdays=+2, holidays=holidays.US())

a = d + relativedelta(bdays=+2, holidays=holidays.US())

print(a)



# a = np.is_busday('2018-11-12')

#HOLIDAYS

# Increment date by two business days
>>> from datetime import date
>>> from bdateutil relativedelta
>>> date(2016, 6, 30) + relativedelta(bdays=+2)
datetime.date(2016, 7, 4)

# If you import date/datetime objects from bdateutil they have a nice
# shortcut to using relativedelta, `add` and `sub` methods:
>>> from bdateutil import date
>>> date(2016, 6, 30).add(bdays=+2)
bdateutil.date(2016, 7, 4)
>>> isinstance(bdateutil.date.today(), datetime.date)
True

# Take into account U.S. statutory holidays
import holidays
date(2018, 11, 11) + relativedelta(bdays=+2, holidays=holidays.US())

datetime.date(2016, 7, 5)

# Take U.S. holidays into account by default whenever
# any bdateutil function is used
# Passing the `holidays` kwarg to a function will take precendent
# over the module default
>>> import bdateutil
>>> import holidays
>>> bdateutil.HOLIDAYS = holidays.US()

# Determine how many business days between two dates
>>> from bdateutil import relativedelta
>>> bdateutil.HOLIDAYS = holidays.US()
>>> r = relativedelta(date(2016, 7, 5), date(2016, 6, 30))
>>> r
relativedelta(days=+5, bdays=+2)
>>> r.bdays
2

# Get a list of the next 10 business days starting 2014-01-01
>>> from bdateutil import rrule, BDAILY
>>> list(rrule(BDAILY, count=10, dtstart=date(2014, 1, 1)))

# Please read detailed documentation below for a complete list of features


