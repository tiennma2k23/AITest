import base64
def img_base64():
    with open("./UI/assets/addfriend/button_1.png", "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    return(my_string)