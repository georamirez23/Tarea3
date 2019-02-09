# Ejemplos sobre listas
# Ejercicio #8

nlista= int(input("Ingrese la cantidad de palabras que desea agregar a la primer lista: "))
list8=[]
if nlista > 0:
    for n in range(nlista):
        palabra= input("Ingrese la " + str(n+1) + " palabra: ")
        list8.insert(n,palabra)
    print(list8)
    print(len(list8))

nlista2 = int(input("Ingrese la cantidad de palabras que desea agregar a la segunda lista: "))
list9 = []
if nlista2 > 0:
    for n2 in range(nlista2):
        palab = input("Ingrese la " + str(n2 + 1) + " palabra: ")
        list9.insert(n2, palab)
    print(list9)
    print(len(list9))

soloprimera=[]
solosegunda=[]
ambas=[]

for r in range(len(list8)):
    if list8[r] in list9[::]:
        ambas.insert(r,list8[r])
    else:
        soloprimera.insert(r,list8[r])
    y=r

for u in range(len(list9)):
    if list9[u] not in list8[::]:
        solosegunda.insert(y,list9[u])

print(ambas)
print(soloprimera)
print(solosegunda)