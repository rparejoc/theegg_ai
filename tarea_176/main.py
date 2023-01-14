#ejercicio 1

numero1 = 3;
numero2 = 5;
numero3 = 10;

if numero1 > numero2 and numero1 > numero3:
    maximo = numero1
elif numero2 > numero1 and numero2 > numero3:
    maximo = numero2
else:
    maximo = numero3

print("El máximo es ", maximo)

#ejercicio 2

frase = "Hola Mundo!!"
print("Longitud de la frase: ", len(frase))

#ejercicio 3
vocales = ["a", "e", "i", "o", "u"];

caracter = "c"

if vocales.__contains__(caracter):
    print("Es una vocal")
else:
    print("No es una vocal")

#ejercicio 4
lista = [1, 2, 3, 4, 5]
suma = 0
for i in range(len(lista)):
    suma += lista[i]

print("La suma de los valores de la lista es: ", suma)

#ejercicio 5

palabra = "reconocer"
reverso = palabra[::-1]

if palabra == reverso:
    print("Es una palindromo")

#ejercicio 6
lista1 = [1, 2, 3, 4, 5]
lista2 = [2, 3, 4, 5, 6]

for i in range(len(lista1)):
    elementoLista1 = lista1[i]
    for j in range(len(lista2)):
        elementoLista2 = lista2[j]
        if elementoLista1 == elementoLista2:
            print(elementoLista1, " aparece en ambas listas")


