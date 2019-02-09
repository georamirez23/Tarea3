# Ejemplos sobre listas
# Ejercicio #5

number5 = int(input("Por favor ingrese la cantidad de palabras que desea asignar a la lista "))
i=1
list5=[]
if number5 > 0:
    for i in range(number5):
        word1= input("Ingrese la palabra # " + " "+ str(i + 1) + ": ")
        list5.insert(i, word1)

    print(len(list5))
    print(list5)
else:
    print("Imposible")



number51= int(input("Por favor ingrese la cantidad de palabras que desea eliminar de la lista "))
ldelete=[]
y=0
if number5> 0:
    for x in range(number51):
        y=0
        wordsdelete = input("Ingrese la " + str(x + 1) + " palabra: ")
        ldelete.insert(x,wordsdelete)
        while y < len(list5):
            if list5[y]== ldelete[x]:
                del(list5[y])
            else:
                y+=1
    print(ldelete)
    print(list5)

else:
    print("Imposible")
else:
    print("Imposible")