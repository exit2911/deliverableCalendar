from pandas.tseries.offsets import BMonthEnd
from datetime import date

d=date.today()

offset = BMonthEnd()

#Last day of current month
offset.rollforward(d)

#Last day of previous month
offset.rollback(d)
