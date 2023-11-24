
class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sumar (self):
        try: 
            self.num1 = int(self.num1)
            self.num2 = int(self.num2)
            suma = self.num1 + self.num2
            return suma
        except ValueError:
            print("No se puede sumar letras")
    def restar (self):
        try:
            self.num1 = int(self.num1)
            self.num2 = int(self.num2)
            restar = self.num1 - self.num2
            return restar
        except ValueError:
            print("No se puede restar letras")
        
    def multiplicar (self):
        try: 
            self.num1 = int(self.num1)
            self.num2 = int(self.num2)
            multiplicar = self.num1 * self.num2
            return multiplicar
        except ValueError:
            print("No se puede multiplicar letras")
    def dividir (self):
        try:
            self.num1 = int(self.num1)
            self.num2 = int(self.num2)
            if self.num2 != 0:
                dividir = self.num1 / self.num2
                return dividir
            else:
                print("No se puede dividir entre cero.")
        except ValueError:
            print("No se puede dividir letras")

    
