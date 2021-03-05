segundos=1
minuto=segundos*60
hora=minuto*60
dia=hora*24
cant_seg=int(input("Ingrese la cantidad de segundos que desea transformar\n"))
print()
print(cant_seg,"segundos es igual a:")
print()
print(cant_seg/minuto,"minutos")
print(cant_seg/hora,"horas")
print(cant_seg/dia,"dias")