
class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sumar (self):
        return self.num1 + self.num2
    def restar (self):
        return self.num1 - self.num2
    def multiplicar (self):
        return self.num1 * self.num2
    def dividir (self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            print("No se puede dividir entre cero.")


    
