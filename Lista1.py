# Ejemplos sobre listas
# Ejercicio #1

number1 = int(input("Ingrese un numero: "))
i=1
list1=[]
if int(number1) > 0:
    for i in range(number1):
        word1= input("Ingrese la palabra: ")
        list1.insert(i,word1)


    print(len(list1))
    for n in range(len(list1)-1):
        print(list1[n])
    print(list1)
else:
    print("Imposible")