x = float(input("Ingrese la cantidad a invertir  "))
y = float(input("Ingrese el interés anual  "))
z = float(input("Ingrese el número de años  "))
capital = x * (1+(y/100)) ** z
capital1 = round(capital,2)
print("El capital obtenido es",capital1)