import qrcode

from qrcode import image 
url = input("¿Que URL desea insertar?") # Pregunta de lo que se quiera que salga en el codigo QR

img = qrcode.make({url})

import os, sys, time, shutil

def textfile():
    file = open("qr.png", "wb")
    x = input("¿Nombre del archivo?")
    img.save(file)
    file.close()
    os.rename("qr.png", "images/{}.png" .format(x))
    file.close()
    print("Su codigo QR ha sido realizado")
        
textfile()
