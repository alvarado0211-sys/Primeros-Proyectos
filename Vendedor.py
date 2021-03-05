sueldo=22000
venta1=int(input("Ingrese su primer venta\n"))
venta2=int(input("Ingrese el valor de la segunda venta\n"))
venta3=int(input("Ingrese el valor de la ultima venta\n"))
total_venta=(venta1+venta2+venta3)
comision=(total_venta*10)/100
ganancia=sueldo+comision
print("El sueldo del vendedor este mes sera de $",ganancia)