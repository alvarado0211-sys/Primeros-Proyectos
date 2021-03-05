print("Bienvenido a su calculadora de ingresos")
print(" ")
inversion=int(input("Ingrese el valor que desea invertir\n"))
tiempo=int(input("¿En cuantos meses desea invertir su capital?\n"))
intereses=inversion*6/100
beneficio=intereses*tiempo
ganancia=inversion+beneficio
print("su ganancia total en ", tiempo,"meses, es de $", ganancia)