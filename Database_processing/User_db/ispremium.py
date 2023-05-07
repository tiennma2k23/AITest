from Database_processing.User_db.get import find_user
from Database_processing.User_db.update_active import update_active

def ispremium(usr):
    __=find_user(usr)
    if (__['status']==False): return True
    else:
        try:
            return __['data']['activate']
        except:
            update_active(__['data']['username'], False)
            return False