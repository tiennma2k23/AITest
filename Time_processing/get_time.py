import time

def get_time():
    now = time.strftime(r"%d/%m/%Y %H:%M:%S",time.localtime())
    return now
    # print("now =", now)
get_time()