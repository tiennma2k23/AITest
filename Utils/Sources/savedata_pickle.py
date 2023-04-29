import pickle
 
# class MyClass():
#     def __init__(self, param):
#         self.param = param
 
def save_object(obj):
    try:
        with open("Appdata/userData/data.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)
 
# obj = MyClass(10)
# save_object({'UID':"10000",'status':"ON"})