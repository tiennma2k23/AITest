
from Database_processing.User_db.get_point_data import get_point_data


arr=get_point_data()

def get_rank_user(usr):
    for x in arr :
        if (x['username']==usr): return x['rank']