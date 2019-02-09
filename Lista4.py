# Ejemplos sobre listas
# Ejercicio #4

number1 = int(input("Por favor ingrese la cantidad de palabras que desea asignar a la lista"))
list4=[]
if int(number1) > 1:
    for i in range(number1):
        word1= input("Ingrese la palabra # " + " "+ str(i + 1) + ": ")
        list4.insert(i,word1)

    print(len(list4))
    print(list4)

    search= str(input("Ingrese la palabra que desea eliminar"))
    xx=number1-1
    for n in range(xx):
        if list4[n] == search:
            del(list4[n])
    print(list4)
else:
    print("Imposible")