"""- Los bucles permiten ejecutar repetidamente un bloque de código mientras se cumpla una condición o durante un número específico de iteraciones.
while: Repite un bloque de código mientras una condición sea verdadera. Si la condición es `False` al comienzo, el bucle no se ejecuta.
."""
contador = 1  # Inicializamos la variable contador en 1
while contador <= 5:  # Mientras el valor de contador sea menor o igual a 5
    print(contador)  # Imprimimos el valor actual de contador
    contador += 1  # Incrementamos el valor de contador en 1
    
""""for: Se utiliza para iterar sobre una secuencia (como una lista, tupla, diccionario, conjunto o cadena), o para ejecutar un bloque de código un número específico de veces"""
for letra in "Python":  # Recorremos cada letra de la palabra "Python"
    print(letra)  # Imprimimos la letra actual
