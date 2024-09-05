#pip install gtts
#py -m pip install gtts

from gtts import gTTS
import os

# Paso 3: Solicitar el Texto al Usuario
texto = input("Ingresa el texto que quieres convertir a voz: ")

# Paso 6: Seleccionar el Idioma
idioma = input("Elige el idioma (es para español, en para inglés, fr para francés): ").lower()

# Paso 4: Convertir el Texto a Voz
tts = gTTS(text=texto, lang=idioma)
archivo_audio = "texto_a_voz.mp3"
tts.save(archivo_audio)

# Paso 5: Reproducir el Archivo de Audio
os.system(f"start {archivo_audio}")
