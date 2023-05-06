import base64
from Utils.Sources.getdata_pickle import load_object
def base64_img():
    __=load_object("Appdata/userData/data.pickle")
    linkk=''
    if (__['status']): linkk=__['data']['img_profile']
    else : 
        return ('')
    imgstring=linkk
    imgdata = base64.b64decode(imgstring)
    filename = 'Appdata/userData/usr_img.jpg'  
    with open(filename, 'wb') as f:
        f.write(imgdata)
    return filename