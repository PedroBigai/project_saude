from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run(debug=True)
