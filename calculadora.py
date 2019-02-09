class Calculadorabasica():
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def suma(self):
        print("El resultado de la suma es: " + str(self.numero1 + self.numero2))

    def restar(self):
        print("El resultado de la resta es: " + str(self.numero1-self.numero2))

    def multiplicacion(self):
        print("El resultado de la multiplicacion es: " + str(self.numero1*self.numero2))

    def division(self):
        print("El resultado de la division es: " + str(self.numero1/self.numero2))

def menu():
    print("****CALCULADORA**** \n Menu\n 1. Suma \n 2. Resta \n 3. Multiplicacion \n 4. División")
    opcion = int(input("Ingrese una opción: "))
    num1 = int(input("Ingrese el primer número: "))
    num2= int(input("Ingrese el segundo número: "))
    cal = Calculadorabasica(num1,num2)
    if opcion ==1:
        cal.suma()
    if opcion==2:
        cal.restar()
    if opcion==3:
        cal.multiplicacion()
    if opcion==4:
        cal.division()

menu()