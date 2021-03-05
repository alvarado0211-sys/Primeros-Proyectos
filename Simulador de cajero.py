print("Bienvenido al cajero automatico de este banco")
print()
usuario=int(input("Ingrese la cantidad de dinero que desea\n"))

cant500 = usuario // 500
resto500 = usuario % 500

cant200 = resto500 // 200
resto200 = resto500 % 200

cant100 = resto200 // 100
resto100 = resto200 % 100

print("cant de billetes de 500: ", cant500)
print()
print("cant de billetes de 200: ", cant200)
print()
print("cant de billetes de 100: ", cant100)
