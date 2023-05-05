import string
import time
from Time_processing.get_time import get_time
from datetime import datetime
def calc_time(time1):
    date_format = r"%d/%m/%Y %H:%M:%S"
    # time1='04/05/2023 09:42:48'
    time2=(get_time())
    # print(time2)
    d0 = datetime.strptime(time1, date_format)
    d1 = datetime.strptime(time2, date_format)
    # print(d0)
    _delta = abs(d0 - d1)
    return (_delta.days)
