from flask import *

import dao

app = Flask(__name__)

app.secret_key = 'ASDdagsd@1'


@app.route('/logout', methods=['POST', 'GET'])
def sair():
    session.pop('login')
    return render_template('index.html')

@app.route('/', methods=['POST', 'GET'])
def pag_principal():
    return render_template('index.html')


@app.route('/fazerlogin', methods=['POST'])
def fazer_login():
    login_user = request.form.get('login')
    senha_user = request.form.get('senha')
    saida =  dao.login(login_user, senha_user)

    if len(saida) > 0:
        return render_template('home.html')
    else:
        return render_template('index.html')

@app.route('/cadastreuser')
def pagcadastro():
    return render_template('pagcad.html')

@app.route('/cadastrarusuario', methods=['POST'])
def cadastraruser():
    nome = request.form.get('nome')
    login = request.form.get('login')
    senha = request.form.get('senha')

    if dao.inserir_user(nome, login, senha):
        msg= 'usuário inserido com sucesso'
        return render_template('index.html', texto=msg)
    else:
        msg = 'Erro ao inserir usuário'
        return render_template('index.html', texto=msg)
@app.route('/doar')
def doarroupa():
    return render_template('pagdoacao.html')

if __name__ == '__main__':
    app.run(debug=True)
