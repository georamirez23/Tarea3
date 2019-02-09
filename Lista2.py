#Ejercicio #2

word1= input("Ingrese la primer palabra: ") #Carmen
word2= input("Ingrese la segunda palabra: ") #Alberto
word3= input("Ingrese la tercer palabra: ") #Benito
word4= input("Ingrese la cuarta palabra: ") #Carmen

list2=[word1,word2,word3,word4]
print(list2)

search= input("Indique la palabra a buscar: ") #Carmen

print(list2.count(search))
print(len(list2))

print(list2[0])
print(list2[1])
print(list2[2])
print(list2[3])

print(list2.index('Alberto'))
print(len(list2))

print(list2[0] + " " + list2[1] + " " + list2[2] + " " + list2[3])
if 'David' in list2[::]:
    print("Si existe en la lista se encuentra en la posición: " + list2.index('David'))
else:
    print("No se encuentra en la lista")