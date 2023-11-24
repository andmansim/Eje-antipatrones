from flask import Flask, render_template, request, flash
from codigobien import Calculadora
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  

@app.route('/home')
def index():
    return render_template('pag.html')


@app.route('/calculadora', methods=['GET', 'POST'])
def calculadora():
    if request.method == 'POST':
        num1 = float(request.form.get('num1'))
        num2 = float(request.form.get('num2'))
        operador = request.form.get('operador')
        
        calculadora = Calculadora(num1, num2)
        if operador == 'sumar':
            resultado = calculadora.sumar()
            mensaje = 'El resultado de la suma es: ' + str(resultado)
            
        elif operador == 'restar':
            resultado = calculadora.restar(num1, num2)
            mensaje = 'El resultado de la resta es: ' + str(resultado)
            
        elif operador == 'multiplicar':
            resultado = calculadora.multiplicar(num1, num2)
            mensaje = 'El resultado de la multiplicacion es: ' + str(resultado)
            
        elif operador == 'dividir':
            resultado = calculadora.dividir(num1, num2)
            mensaje = 'El resultado de la division es: ' + str(resultado)
            
        else:
            mensaje = 'No se ha seleccionado una operacion'
            
        flash(mensaje, 'success')
    return render_template('mensaje_resultados.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)