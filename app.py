
from flask import Flask, jsonify, request

app = Flask(__name__)

conquistas = [
    {"id": 1, "nome": "Primeira conquista", "coins": 100},
    {"id": 2, "nome": "Jogador iniciante", "coins": 200}
]

# Rota inicial
@app.route("/")
def inicio():
    return jsonify({
        "mensagem": "Minha API Python está funcionando!"
    })

# Consultar conquistas
@app.route("/api/conquistas", methods=["GET"])
def listar_conquistas():
    return jsonify(conquistas)

# Cadastrar conquista
@app.route("/api/conquistas", methods=["POST"])
def cadastrar_conquista():
    dados = request.get_json()

    nova = {
        "id": len(conquistas) + 1,
        "nome": dados["nome"],
        "coins": dados["coins"]
    }

    conquistas.append(nova)

    return jsonify(nova), 201

if __name__ == "__main__":
    app.run(debug=True)
