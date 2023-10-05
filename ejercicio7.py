x = float(input("Introduce tu peso en kg  "))
y = float(input("Introduce tu estatura en metros  "))
imc = x/y**2
imc = round(imc,2)
print("Tu índice de masa corporal es",imc)