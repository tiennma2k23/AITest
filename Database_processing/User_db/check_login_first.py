from Database_processing.User_db.get import find_user
from Database_processing.User_db.update_login_first import update_login_first

def check_login_first(usr):
    __=find_user(usr)
    if (__['status']==False): return True
    else:
        try:
            return __['data']['first_login']
        except:
            update_login_first(__['data']['username'], False)
            return False