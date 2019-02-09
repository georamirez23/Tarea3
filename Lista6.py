#Ejercicio 6
nlista= int(input("Ingrese la cantidad de palabras que desea agregar a la lista: "))
list6=[]
if nlista > 0:
    for n in range(nlista):
        palabra= input("Ingrese la " + str(n+1) + " palabra: ")
        list6.insert(n,palabra)

    print(list6)
reversolista = list6[::-1]
print(reversolista)