def salto_linea():
	print()

print("Bienvenido a su generador de claves")
salto_linea()
caracteres="ABCDEFGHJIKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@#$_&-+/*!?" ##caracteres que se incluiran en la constraseña
while True:
	import time
	print("¿Que desea hacer?")				
	print("OPCION A: GENERAR CLAVE")
	print("OPCION B: SALIR DEL PROGRAMA") 			##opcion de salida por comando
	opcion=str(input())
	if opcion=="A" or opcion=="a":
		import random
		import string
		longitud=int(input("Indique la longitud de su contraseña:\n")) ##indicamos la longitud de la contraseña
		salto_linea()
		contraseña=("").join(random.choice(caracteres)for i in range(longitud)) ## en base a la longitud genera un string con los caracteres
		print("GENERANDO CLAVE...")
		time.sleep(0.3)
		salto_linea()
		print("SU CONTRASEÑA SEGURA ES: ",contraseña)			##imprime la contraseña segura
		salto_linea()
	if opcion=="B" or opcion=="b":					##la opcion B para salir del programa
		print("SALIENDO DEL PROGRAMA...")
		time.sleep(0.5)
		break									## sale del ciclo y termina el programa