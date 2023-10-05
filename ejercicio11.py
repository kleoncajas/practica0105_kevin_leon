x = float(input("Ingrese la cantidad inicial  "))
interés1 = (x * 0.04) + x
interés1_1 = round(interés1,2)
interés2 = (interés1 * 0.04) + interés1
interés2_1 = round(interés2,2)
interés3 = (interés2 * 0.04) + interés2
interés3_1 = round(interés3,2)
print("La cantidad de ahorro por año")
print("Año 1",interés1_1)
print("Año 2",interés2_1)
print("Año 3",interés3_1)