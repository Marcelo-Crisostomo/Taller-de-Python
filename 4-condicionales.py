#Condicionales  ----------
#OPREACIONES CONDICIONALES 
"""Las condicionales son estructuras en programación que permiten ejecutar diferentes bloques de código dependiendo de si una condición es verdadera o falsa. Los más comunes son if, else y elif, y se usan para tomar decisiones dentro de un programa."""

# Uso de if/else para tomar decisiones
"""- Las estructuras condicionales son fundamentales para la toma de decisiones en programación. Permiten que el programa ejecute diferentes bloques de código dependiendo de si una condición es verdadera o falsa.
- if: Comprueba si una condición es verdadera. Si lo es, ejecuta el bloque de código que sigue.
- elif: (opcional) Se usa para comprobar múltiples condiciones si la primera es falsa.
- else: Ejecuta un bloque de código si todas las condiciones anteriores son falsas."""

temperatura = int(input("¿Cuál es la temperatura actual en grados Celsius? "))

if temperatura > 30:  # Si la temperatura es mayor a 30 grados
    print("Hace mucho calor afuera.")  # Imprimimos este mensaje
elif temperatura >= 20:  # Si no es mayor a 30 pero sí mayor o igual a 20
    print("El clima es agradable.")  # Imprimimos este mensaje
else:  # Si ninguna de las condiciones anteriores se cumple
    print("Hace frío afuera.")  # Imprimimos este mensaje

    