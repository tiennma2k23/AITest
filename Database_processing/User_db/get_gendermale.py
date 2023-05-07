from Database_processing.User_db.get import find_user
from Database_processing.User_db.update import update_user

def get_gendermale(usr):
    __=find_user(usr)
    if (__['status']==False): return True
    else:
        try:
            _status=__['data']['gendermale']
            return _status
        except:
            update_user(__['data']['username'], {
                'gendermale': True
            })
            return True
