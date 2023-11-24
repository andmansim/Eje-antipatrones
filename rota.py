from flask import Flask, render_template, request, redirect, url_for, flash
from codigobien import Calculadora

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('pag.html')


@app.route('calculadora', methods=['GET', 'POST'])
def calculadora():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operador = request.form['operador']
        calculadora = Calculadora(num1, num2)
        if operador == 'suma':
            resultado = calculadora.sumar()
            flash('El resultado de la suma es: ' + str(resultado))
            return redirect(url_for('calculadora'))
        elif operador == 'resta':
            resultado = calculadora.restar(num1, num2)
            flash('El resultado de la resta es: ' + str(resultado))
            return redirect(url_for('calculadora'))
        elif operador == 'multiplicar':
            resultado = calculadora.multiplicar(num1, num2)
            flash('El resultado de la multiplicacion es: ' + str(resultado))
            return redirect(url_for('calculadora'))
        elif operador == 'dividir':
            resultado = calculadora.dividir(num1, num2)
            flash('El resultado de la division es: ' + str(resultado))
            return redirect(url_for('calculadora'))
        else:
            flash('No se ha seleccionado una operacion')
            return redirect(url_for('calculadora'))
    return render_template('calculadora.html')

if __name__ == '__main__':
    app.run(debug=True)