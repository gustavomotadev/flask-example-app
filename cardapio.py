from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/cardapio')
def mostrar_cardapio():
    return render_template('cardapio.html')

@app.route('/cardapio/pizza')
def mostrar_pizza():
    return render_template('pizza.html')

@app.route('/cardapio/hamburguer')
def mostrar_hamburguer():
    return render_template('hamburguer.html')

if __name__ == '__main__':
    app.run(debug=True)