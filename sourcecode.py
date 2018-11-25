"""
DEAL: Clear Creek

monthly: 10th BD
pmt: 20th or next BD
pmt_posting: pmt date - 1
LIBOR: 2BD prior to posting
    
    

"""
import datetime
import numpy as np
import holidays
from bdateutil import relativedelta


dates = []


def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  
    return next_month - datetime.timedelta(days=next_month.day)

def end_of_month_list():
    

    
    for month in range(1, 13):
        end_date = last_day_of_month(datetime.date(2018, month, 1))
        dates.append(end_date)
    return dates


def pmt():
    for month in range(1, 13):
        pmt_date = last_day_of_month(datetime.date(2018, month, 1))+ datetime.timedelta(days = 20)
       
        if np.is_busday(pmt_date):
            print("pmt due",(pmt_date))
            if np.is_busday(pmt_date + datetime.timedelta(days = -1)):
                print("pmt post",pmt_date + datetime.timedelta(days = -1))
            else:   
                print("pmt post",pmt_date + datetime.timedelta(days = -3))
        else:
            if np.is_busday(pmt_date + datetime.timedelta(days = 1)):
                print("pmt due",pmt_date + datetime.timedelta(days = 1))
                print("pmt post",(pmt_date + datetime.timedelta(days = 1)) + relativedelta(bdays=-1, holidays=holidays.US()))
            
def monthly():  
    
    for i in dates:
        due_date = i + relativedelta(bdays=+10, holidays=holidays.US())
        print("monthly due",due_date)
            
        
end_of_month_list()

monthly()

pmt()
