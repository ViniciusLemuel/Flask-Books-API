from flask import Flask, jsonify, request

app = Flask("__name__")

livros = [
    { 
        'id': 1, 
        'autor': 'Patrick Ness',
        'título': 'Mundo em Caos'
    },
    {
        'id': 2,
        'autor': 'V.E. Schwab',
        'título': 'Vilão'
    },
    {
        'id': 3,
        'autor': 'George S. Clason',
        'título': 'O homem mais rico da babilônia' 
    }
]

# - Consultar (todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# - Consultar (id)
@app.route('/livros/<int:id>', methods= ['GET'])
def obter_livros_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# - Incluir livro
@app.route('/livros', methods = ['POST'])
def incluir_novo_livro(): 
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

# - Editar
@app.route('/livros/<int:id>', methods= ['PUT'])
def editar_livros(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# - Excluir
@app.route('/livros/<int:id>', methods= ['DELETE'])
def excluir_livro(id):
    for indice, id, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

app.run(port=5000, host='localhost', debug=True)