import base64
from img_base64 import img_base64
imgstring=img_base64()
imgdata = base64.b64decode(imgstring)
filename = 'Appdata/userData/usr_img.jpg'  
with open(filename, 'wb') as f:
    f.write(imgdata)