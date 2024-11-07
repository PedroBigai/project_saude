from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('pag_login/login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('pag_cadastro/cadastro.html')

@app.route('/pag_principal')
def pag_principal():
    return render_template('pag_principal/pag_principal.html')

@app.route('/pag_user')
def pag_user():
    return render_template('pag_user/pag_user.html')





# ROTAS API LOCAL

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    # Aqui você pode processar os dados
    usuario = data.get('usuario')
    email = data.get('email')
    senha = data.get('senha')
    altura = data.get('altura')
    dataNas = data.get('data')
    peso = data.get('peso')
    sexo = data.get('sexo')
    objetivo = data.get('objetivo')


    print(data)    # Faça o que for necessário com os dados (armazenar no banco, etc.)

    return jsonify({"message": "Usuário registrado com sucesso!"}), 201


if __name__ == '__main__':
    app.run(debug=True)
