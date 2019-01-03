import base64
import PySimpleGUI as Sg
from os import listdir

image_folder = Sg.PopupGetFolder("Select image Folder", default_path="C:/")
save_base64 = open("{}/savedBase64list6.txt".format(image_folder), 'a+')

for image_file in listdir(image_folder):
    opened_image = open("{}/{}".format(image_folder, image_file), 'rb+')
    base64_image = base64.b64encode(opened_image.read())
    save_base64.write("\n")
    save_base64.write("{}".format(image_file))
    save_base64.write(str(base64_image))
    save_base64.write("\n")
    opened_image.close()

save_base64.close()
