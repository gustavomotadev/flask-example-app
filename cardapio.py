from flask import Flask, render_template, abort
from http import HTTPStatus
from json import load

with open('banco.json', 'r', encoding='utf-8') as arquivo_json:
    banco = load(arquivo_json)

app = Flask(__name__)

@app.errorhandler(HTTPStatus.NOT_FOUND)
def page_not_found(erro):
   return render_template('404.jinja'), HTTPStatus.NOT_FOUND

@app.route('/')
@app.route('/index')
@app.route('/cardapio')
def mostrar_cardapio():
    return render_template('cardapio.jinja', banco=banco)

@app.route('/cardapio/<alimento>')
def mostrar_alimento(alimento: str):
    dados = banco.get(alimento)
    if dados:
        return render_template('alimento.jinja', 
            nome=dados['nome'], 
            descricao=dados['descricao'],
            codigo=dados['codigo'],
            url_imagem=dados['url_imagem'])
    else:
        abort(HTTPStatus.NOT_FOUND)

if __name__ == '__main__':
    app.run(debug=True)