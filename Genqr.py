import qrcode

from qrcode import image 
url = input("¿Que URL desea insertar?") # Pregunta de lo que se quiera que salga en el codigo QR

img = qrcode.make({url})

import os, sys, time

def textfile():
    f = open("qr.png", "wb")
    x = input("¿Nombre del archivo?")
    img.save(f)
    f.close()
    os.rename("qr.png", "{}.png".format(x))
    f.write("url it's ok?")
    f.close()

textfile()
