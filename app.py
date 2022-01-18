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

        # Exibe novamente todos os itens no carrinho de compras
        return make_response(jsonify('Item criado por formulario',carrinho), 200)
        
    # Se a requisição vir por meio de um JSON
    # ex: >> curl -X POST 127.0.0.1:5000/post/ -H "Content-Type: application/json" -d '{\"nome\":\"notebook avell\"}'
    else:
    
        # Extrai o conteúdo do corpo da requisição JSON
        body = request.get_json()

        # Se o body estiver vazio
        if not body:
            return make_response(jsonify({"erro":"Nome invalido"}), 400)

        # Extrai o valor de "nome" na requisição do JSON
        # Extrai o valor de "nome" no corpo extraído
        nome = body['nome']
        
        # Se o valor de nome for um valor inválido
        if not nome:
            return make_response(jsonify({"erro":"Nome invalido"}), 400)

        novo_item = {
            # Incremento do id: valor do ID do último item do carrinho
            # somado com 1
            'id': carrinho[-1]['id'] + 1,
            # Nome extraído da requisição
            'nome': nome
        }

        # Insere no final do carrinho o novo item criado
        carrinho.append(novo_item)

        # Exibe novamente todos os itens no carrinho de compras
        return make_response(jsonify('Item criado por JSON',carrinho), 200)
    # ----------------------------------------------------------------------------

@app.route('/put/<int:id>', methods=['PUT'])
def put(id):

    body = request.get_json()

    if not body:
        return make_response(jsonify({"erro":"Nome invalido"}), 400)

    # Para cada item no carrinho, procure por um com determinado ID
    item = [item for item in carrinho if item['id'] == id]

    if len(item) == 0:
        novo_item = {
            # Incremento do id: valor do ID do último item do carrinho
            # somado com 1
            'id': id,
            # Nome extraído da requisição
            'nome': body['nome']
        }
        carrinho.append(novo_item)
        return make_response(jsonify(carrinho), 200)

    item[0]['nome'] = body['nome']

    return make_response(jsonify(carrinho), 200)

# @app.route('/patch')
# def patch():
#     return ...

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):

    # Para cada item no carrinho, procure por um com determinado ID
    item = [item for item in carrinho if item['id'] == id]

    if item:
        carrinho.remove(item[0])
        return make_response(jsonify(carrinho), 201)

    return make_response(jsonify({"erro":"Item nao encontrado"}), 404)
    

if __name__ == '__main__':
    app.run(debug=True)
