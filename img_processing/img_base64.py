import base64
def img_base64(url):
    with open(url, "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    return(my_string)
