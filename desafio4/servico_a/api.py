from flask import Flask, jsonify
meuApp = Flask(__name__)

@meuApp.route('/lista')
def mostrarLista():
    return jsonify({"nomes": ["Carlos", "Maria", "Joao"]})

if __name__ == "__main__":
    meuApp.run(host='0.0.0.0', port=5000)