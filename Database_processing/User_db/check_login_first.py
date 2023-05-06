from Database_processing.User_db.get import find_user


def check_login_first(usr):
    __=find_user(usr)
    if (__['status']==False): return True
    else:
        return __['data']['first_login']