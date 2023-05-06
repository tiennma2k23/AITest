from Database_processing.User_db.get import find_user


def get_gendermale(usr):
    __=find_user(usr)
    if (__['status']==False): return True
    else:
        _status=__['data']['gendermale']
        return _status