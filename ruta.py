from flask import Flask, render_template, request, flash
from codigocalculadora import Calculadora
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  

@app.route('/home')
def index():
    return render_template('pagCalculadora.html')


@app.route('/calculadora', methods=['GET', 'POST'])
def calculadora():
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        operador = request.form.get('operador')

        calculadora = Calculadora(num1, num2)
        if operador == 'sumar':
            resultado = calculadora.sumar()
 
        elif operador == 'restar':
            resultado = calculadora.restar()

        elif operador == 'multiplicar':
            resultado = calculadora.multiplicar()
            
        elif operador == 'dividir':
            resultado = calculadora.dividir()
        
        mensaje = 'El resultado es: ' + str(resultado)
        flash(mensaje, 'success')
    return render_template('mensaje_resultados.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)