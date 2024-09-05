#Comparaciones:
"""  == es igual a
- != no es igual a
- > mayor que
- < menor que
- >= mayor o igual que
- <= menor o igual que  """

#Operadores lógicos:
""" and: Todas las condiciones deben ser verdaderas.
or: Al menos una condición debe ser verdadera.
not: Invierte el valor de verdad de una condición.    """


tiene_ticket = True
edad = 20
expulsado_del_cine = False
"""Supongamos que estamos evaluando el acceso a una sala de cine, basado en tres condiciones:

Acceso 1: si tienes un ticket y eres mayor de 18 años.
Acceso 2: si no tienes ticket, pero eres mayor de 60 años (entrada gratuita para mayores de 60).
Acceso 3: si no has sido expulsado del cine antes."""
# Operación lógica con AND, OR y NOT
if tiene_ticket and edad >= 18:
    print("Puedes entrar al cine.")
elif not tiene_ticket and edad > 60:
    print("Puedes entrar gratis por ser mayor de 60.")
elif not expulsado_del_cine:
    print("Puedes entrar porque no has sido expulsado.")
else:
    print("No puedes entrar.")