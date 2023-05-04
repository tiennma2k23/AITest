from Database_processing.Friends_db.get_friends import get_fr_by_username
from Database_processing.Friends_db.update_fr import update_fr_user
from Utils.Sources.getdata_pickle import load_object


def delete_fr(usr):
    _db=load_object("Appdata/userData/data.pickle")
    _username="abc"
    if(_db['status']):
        _username=_db['data']['username']
        __fr=get_fr_by_username(_username)
        __fr.remove(usr)
        update_fr_user(_username,__fr)
        ___fr=get_fr_by_username(usr)
        ___fr.remove(_username)
        update_fr_user(usr,___fr)
    