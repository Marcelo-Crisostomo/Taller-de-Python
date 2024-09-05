#primero instala desde consola 
#pip install qrcode
#pip install pillow
#py -m pip install qrcode
#https://www.duoc.cl/escuela/informatica-telecomunicaciones/
import qrcode
from PIL import Image

# Paso 3: Solicitar el Texto o Enlace al Usuario
datos = input("Ingresa el texto o URL que quieres convertir a un código QR: ")

# Paso 4: Generar el Código QR
qr = qrcode.make(datos)

# Paso 5: Guardar el Código QR como Imagen
nombre_archivo = input("Ingresa el nombre del archivo de imagen (sin extensión): ")
nombre_archivo += ".png"
qr.save(nombre_archivo)

# Paso 6: Abrir y Mostrar el Código QR
imagen = Image.open(nombre_archivo)
imagen.show()
