from flask import Flask, render_template, request, flash
from codigocalculadora import Calculadora
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  

#Ruta de la página principal
@app.route('/home')
def index():
    return render_template('pagCalculadora.html')

#Ruta calcular
@app.route('/calculadora', methods=['GET', 'POST'])
def calculadora():
    if request.method == 'POST':
        #recogemos los datos del formulario
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        operador = request.form.get('operador')

        #creamos el objeto calculadora
        calculadora = Calculadora(num1, num2)
        
        #identificamos el operador y llamamos a la función correspondiente
        if operador == 'sumar':
            resultado = calculadora.sumar()
            
        elif operador == 'restar':
            resultado = calculadora.restar()

        elif operador == 'multiplicar':
            resultado = calculadora.multiplicar()
            
        elif operador == 'dividir':
            resultado = calculadora.dividir()
        
        #mensaje para mostrar el resultado
        mensaje = 'El resultado es: ' + str(resultado)
        flash(mensaje, 'success')
    return render_template('mensaje_resultados.html', mensaje=mensaje)

