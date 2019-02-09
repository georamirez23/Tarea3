# Ejemplos sobre listas
# Ejercicio #7

nlista= int(input("Ingrese la cantidad de palabras que desea agregar a la lista: "))
list7=[]
if nlista > 0:
    for n in range(nlista):
        palabra= input("Ingrese la " + str(n+1) + " palabra: ")
        list7.insert(n,palabra)
    print(list7)
    list7= set(list7[::])
    print(list7)

