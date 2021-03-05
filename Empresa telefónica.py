print("Buenas tardes")
print()
comunicacion = 7
segundo_llamada= 0.5
cantidad_llamadas=int(input("Ingrese cuantas llamadas realizo el cliente\n"))
print()
tiempo_llamada=int(input("Ingrese cuantos segundos duraron las llamadas del cliente\n"))
costo_cliente= (comunicacion*cantidad_llamadas) + (segundo_llamada*tiempo_llamada)
print()
print("El cliente debe abonar $",costo_cliente)
