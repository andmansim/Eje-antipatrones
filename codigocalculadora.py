
class Calculadora:
    '''
    Clase Calculadora encargada de revisar los datos ingresados por el usuario y 
    realizar las operaciones correspondientes.
    '''
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sumar (self):
        #Miramos si los datos ingresados son números y si no, devolvemos un mensaje de error
        try: 
            self.num1 = float(self.num1)
            self.num2 = float(self.num2)
            #realizamos la operación
            suma = self.num1 + self.num2
            return suma
        except ValueError:
            return("No se puede sumar letras")
    def restar (self):
        #Miramos si los datos ingresados son números y si no, devolvemos un mensaje de error
        try:
            self.num1 = float(self.num1)
            self.num2 = float(self.num2)
            #realizamos la operación
            restar = self.num1 - self.num2
            return restar
        except ValueError:
            return("No se puede restar letras")
        
    def multiplicar (self):
        #Miramos si los datos ingresados son números y si no, devolvemos un mensaje de error
        try: 
            self.num1 = float(self.num1)
            self.num2 = float(self.num2)
            #realizamos la operación
            multiplicar = self.num1 * self.num2
            return multiplicar
        except ValueError:
            return("No se puede multiplicar letras")
        
    def dividir (self):
        #Miramos si los datos ingresados son números y si no, devolvemos un mensaje de error
        try:
            self.num1 = float(self.num1)
            self.num2 = float(self.num2)
            #miramos si el divisor es cero y si no, realizamos la operación
            if self.num2 != 0:
                dividir = self.num1 / self.num2
                return dividir
            else:
                return("No se puede dividir entre cero.")
        except ValueError:
            return("No se puede dividir letras")

    
