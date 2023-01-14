lado = int(input("Introduce el lado del cuadrado: "))

if lado <= 0:
    print("El lado debe de ser mayor que 0")
else:
    area = lado ** 2
    print("El area es " + str(area))