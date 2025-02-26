
# pedi info al usuario por consola
nombre = input("Como te llamas? ")
# imprime el nombre en consola
print("hola :",nombre)
# generamos un texto para la pregunta
texto = "Cuantas horas has trabajado? " + nombre +":"

horas = int(input(texto))
# calculamos el sueldo

# calulo_sueldo = horas * 50

print("Sueldo a pagar a" ,"es de :",  horas * 50 ,  "U$D")

print("#"*50)
print("Fin del programa")