num = 677.00 

print("\n \t ------ PROBLEMA 1 --------------")

nom = input("\nIngrese su nombre: ")
print("\n \t Calcular las ventas ")
vent1 = float(input("\nIngrese el valor de la primera venta: "))
vent2 = float(input("Ingrese el valor de la segunda venta: "))
vent3 = float(input("Ingrese el valor de la tercera venta: "))
vent4 = float(input("Ingrese el valor de la cuarta venta: "))
vent5 = float(input("Ingrese el valor de la quinta venta: "))

sumar = vent1 + vent2 + vent3 + vent4 + vent5 

if sumar > num:
    print("\nEs mayor al promedio de ventas diarias")
else:
    print("\nEs menor al promedio de ventas diarias")

print("\n \n ------------------ PROBLEMA 2 ----------------------")

d = "dolares"
c = "colones"
l = "lempiras"
p = "colombianos"

nom2 = input("\nIngrese su nombre: ")
chain1 = input("¿Cual es la moneda que desea cambiar? \n\nA. dolares \nB. colones \nC. lempiras \nD. colombianos \n\nIngrese el nombre: ")
chain = float(input("¿Cuanto desea cambiar? ")) 

if chain1 == d:
    calc1 = chain / 1.21
    print(f"\nMuchas gracias {nom2} por su visita, su cambio en dolares seria de {calc1:.2f}")
    print("\nMuchas gracias") 

elif chain1 == c:
    calc2 = chain / 738.59
    print(f"\nMuchas gracias {nom2} por su visita, su cambio en colones seria de {calc2:.2f}")
    print("\nMuchas gracias") 

elif chain1 == l:
    calc3 = chain / 29.16
    print(f"\nMuchas gracias {nom2} por su visita, su cambio en lempira seria de {calc3:.2f}")
    print("\nMuchas gracias") 

elif chain1 == p: 
    calc4 = chain / 4.314
    print(f"\nMuchas gracias {nom2} por su visita, su cambio en pesos colombianos seria de {calc4:.2f}")
    print("\nMuchas gracias") 


    

