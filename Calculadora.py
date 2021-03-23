import time

## Presento la calculadora y sus opciones
print("Bienvenido a su calculadora personal")

print("1 - SUMA\n2 - RESTA\n3 - MUTLIPLICACION\n4 - DIVISION\n5 - SALIR DEL PROGRAMA")
print()
operacion=str(input("Ingrese el numero de la operacion deseada: "))
print()
while operacion<="5" and operacion>="1":                    ##abrimos el ciclo para que la calculadora se inicie luego de cada operacion
    if operacion== "1":                         ##ingresando esta opcion sumamos cualquier numero
        num1=float(input("Ingrese un numero: "))
        num2=float(input("Ingrese un segundo numero: "))
        time.sleep(0.2)
        print()
        print("El resultado de la suma es=",num1+num2)
        print()
        print("1 - SUMA\n2 - RESTA\n3 - MUTLIPLICACION\n4 - DIVISION\n5 - SALIR DEL PROGRAMA")
        print()
        operacion=str(input("Ingrese el numero de la operacion deseada: "))
    elif operacion== "2":               ##esta es la opcion para las restas
        num1=float(input("Ingrese un numero: "))
        num2=float(input("Ingrese un segundo numero: "))
        time.sleep(0.2)
        print()
        print("El resultado de la resta es=",num1-num2)
        print()
        print("1 - SUMA\n2 - RESTA\n3 - MUTLIPLICACION\n4 - DIVISION\n5 - SALIR DEL PROGRAMA")
        print()
        operacion=str(input("Ingrese el numero de la operacion deseada: "))
    elif operacion== "3":           ## esta es la opcion para las multiplicaciones
        num1=float(input("Ingrese un numero: "))
        num2=float(input("Ingrese un segundo numero: "))
        time.sleep(0.2)
        print()
        print("El resultado de la multiplicación es=",num1*num2)
        print()   
        print("1 - SUMA\n2 - RESTA\n3 - MUTLIPLICACION\n4 - DIVISION\n5 - SALIR DEL PROGRAMA")
        print()
        operacion=str(input("Ingrese el numero de la operacion deseada: "))
    elif operacion== "4":                           ## esta es la opcion para realizar divisiones
        num1=float(input("Ingrese un numero: "))
        num2=float(input("Ingrese un segundo numero: "))
        time.sleep(0.2)
        print()
        print("El resultado de la division es=",num1/num2)
        print()
        print("1 - SUMA\n2 - RESTA\n3 - MUTLIPLICACION\n4 - DIVISION\n5 - SALIR DEL PROGRAMA")
        print()
        operacion=str(input("Ingrese el numero de la operacion deseada: "))    
    elif operacion== "5":               ## esta opcion finaliza y cierra el programa
        print("El programa ha finalizado")
        time.sleep(0.5)
        break                               ##fin del ciclo while
