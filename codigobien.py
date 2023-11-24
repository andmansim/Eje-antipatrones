def calcular(operacion, num1, num2):
    try: 
        if operacion == 'suma':
            return num1 + num2
        elif operacion == 'resta':
            return num1 - num2
        elif operacion == 'multiplicacion':
            return num1 * num2
        elif operacion == 'division':
            if num2 != 0:
                return num1 / num2
            else:
                print("No se puede dividir entre cero.")
        else:
            raise ValueError("Operación no soportada.")
    except ValueError as e:
        print(f'Error: {e}')
    
