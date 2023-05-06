import base64
from Utils.Sources.getdata_pickle import load_object
def base64_img(url):
    __=load_object("Appdata/userData/data.pickle")
    linkk=''
    if (__['status']): linkk=__['data']['img_profile']
    else:
        raise FileNotFoundError
    imgstring=linkk
    imgdata = base64.b64decode(imgstring)
    filename = 'Appdata/userData/'+url
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()
    return filename

def base64_img_with_base64url(link,url):
    imgstring=link
    imgdata = base64.b64decode(imgstring)
    filename = 'Appdata/userData/'+url
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()
    return filename

        