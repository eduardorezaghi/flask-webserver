from flask import Flask
from flask import render_template
from flask import request, make_response, jsonify

# CARRINHO: Banco de Dados fictício
# Representa um carrinho de compras, com seus itens
#  contendo id e nome

carrinho = [
    {
        "id":1,
        "nome":"notebook lenovo"
    },
    {
        "id":2,
        "nome":"dvd player"
    },
]

# Variáveis de ambiente da aplicação Flask
# >> $env:FLASK_ENV = "development"
# >> $env:FLASK_APP = "app"
app = Flask(__name__)


# ROTAS GET
# ----------------------------------------------------------------------------

# Retorna uma representação JSON do carrinho de compras
@app.route('/')
def get_carrinho():
    return make_response(jsonify(carrinho), 200)

# Retorna um item específico em formato JSON do carrinho de compras
@app.route('/<int:id>', methods=['GET'])
def get_carrinho_item(id):

    # Para cada item no carrinho, procure por um com determinado ID
    item = [item for item in carrinho if item['id'] == id]

    # Se não foi encontrado nenhum item com dado ID,
    # retorne uma mensagem de erro em formato JSON
    if len(item) == 0:
        return make_response(jsonify({"erro":"Item nao encontrado"}), 404)

    # Se o item foi encontrado, retorne sua representação como
    # JSON
    return make_response(jsonify({"Item": item[0]}), 200)
# ----------------------------------------------------------------------------


if __name__ == '__main__':
    app.run(debug=True)
