from flask import Flask, render_template, request, flash
from codigobien import Calculadora

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('pag.html')


@app.route('/calculadora', methods=['GET', 'POST'])
def calculadora():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operador = request.form['operador']
        calculadora = Calculadora(num1, num2)
        if operador == 'sumar':
            resultado = calculadora.sumar()
            mensaje = 'El resultado de la suma es:' + str(resultado)
            flash(mensaje, 'success')
            
        elif operador == 'restar':
            resultado = calculadora.restar(num1, num2)
            mensaje = 'El resultado de la resta es:' + str(resultado)
            flash(mensaje, 'success')
            
        elif operador == 'multiplicar':
            resultado = calculadora.multiplicar(num1, num2)
            mensaje = 'El resultado de la multiplicacion es:' + str(resultado)
            flash(mensaje, 'success')
            
        elif operador == 'dividir':
            resultado = calculadora.dividir(num1, num2)
            mensaje = 'El resultado de la division es:' + str(resultado)
            flash(mensaje, 'success')            
        else:
            mensaje = 'No se ha seleccionado una operacion'
            flash(mensaje, 'success')
            
    return render_template('pag.html')

if __name__ == '__main__':
    app.run(debug=True)