"""Entrada y Salida de Datos
input(): Esta función se usa para obtener datos del usuario. Siempre devuelve el valor como una cadena de texto (str). Es importante recordar que si el usuario ingresa un número y quieres usarlo en cálculos, necesitarás convertirlo a un tipo numérico (por ejemplo, usando int() o `float()`).
- print(): Esta función se usa para mostrar datos al usuario. Puede mostrar cadenas, números y resultados de operaciones, y permite formatear la salida para que sea más legible."""


# Pedir al usuario su nombre
nombre = input("¿Cómo te llamas? ")  # 'input' guarda el dato ingresado como cadena de texto
print("Hola, " + nombre + "! Bienvenido/a al taller de Python.")  # Concatenamos y mostramos un mensaje

# Pedir la edad y realizar un cálculo
edad = input("¿Cuántos años tienes? ")  # 'input' devuelve siempre una cadena
edad = int(edad)  # Convertimos la cadena a entero para poder realizar operaciones matemáticas
print("El próximo año tendrás " + str(edad + 1) + " años.")  # Sumamos 1 y convertimos el resultado de nuevo a cadena


#### **Formateo de Cadenas (f-strings):**Desde Python 3.6, se introdujo el uso de **f-strings** para formatear cadenas de manera más legible y directa.

nombre = "Ana"
edad = 30
print(f"Hola, {nombre}. Tienes {edad} años.")  # Usamos f-strings para insertar variables dentro de la cadena

