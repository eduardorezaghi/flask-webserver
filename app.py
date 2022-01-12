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

# ROTAS POST
# ----------------------------------------------------------------------------

# Retorna a atualização do carrinho com o novo item adicionado por POST
@app.route('/post/', methods=["GET","POST"])
def post_form():
    if request.method == 'GET':
        # Renderiza um formulário para inserção de dados
        return render_template('form.html')
    
    # Se a requisição vir de um formulário
    if request.form:

        # Extrai o valor de "nome" na requisição do formulário
        nome = request.form['nome']
        
        # Se o valor de nome for um valor inválido
        if not nome:
            return make_response(jsonify({"erro":"Item invalido"}), 404)

        # Criação de um novo item
        novo_item = {
            # Incremento do id: valor do ID do último item do carrinho
            # somado com 1
            'id': carrinho[-1]['id'] + 1,
            # Nome extraído da requisição
            'nome': nome
        }

        # Insere no final do carrinho o novo item criado
        carrinho.append(novo_item)

    # Se a requisição vir por meio de um JSON
    # ex: >> curl -d "nome=cd player" -X POST http://127.0.0.1:5000/post/
    else:
        # Extrai o valor de "nome" na requisição do JSON
        nome = request.json['nome']
        
        # Se o valor de nome for um valor inválido
        if not nome:
            return make_response(jsonify({"erro":"Item invalido"}), 404)

    # Exibe novamente todos os itens no carrinho de compras
    return make_response(jsonify(carrinho), 200)
# ----------------------------------------------------------------------------

# @app.route('/put')
# def put():
#     return ...

# @app.route('/patch')
# def patch():
#     return ...

# @app.route('/delete')
# def delete():
#     return ...

if __name__ == '__main__':
    app.run(debug=True)
