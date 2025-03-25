from marcelo import bisiesto

nombre = input("Ingrese su nombre: ")
año = int(input("Ingrese su año de nacimiento: "))
if bisiesto(año):
    print(f"{nombre}, naciste en un año bisiesto.")
else:
    print(f"{nombre}, naciste en un año no bisiesto.")
