import pickle
 

def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return {'status':True,'data':pickle.load(f)}
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)
        return {'status':False,'data':''}
 
# obj = load_object("data.pickle")
 
# print(obj)