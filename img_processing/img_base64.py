import base64
def img_base64():
    with open("./Appdata/userData/usr_img.jpg", "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    return(my_string)
