from flask import *

import dao

app = Flask(__name__)

app.secret_key = 'KH39jdkxl9#$%&%$AGkejhf '


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
        session['login'] = login_user
        nome_user = saida[0][0]
        return render_template('home.html', nome=nome_user)
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

    if dao.inserir_user(nome,login,senha):
        msg = 'Erro ao cadastrar usuario'
        return render_template('index.html', texto=msg)
    else:
        msg = 'usuario inserido com sucesso'
        return render_template('index.html', texto=msg)


@app.route('/cadastrardoacao', methods=['POST'])
def cadastrarroupa():
    if 'login' in session:
        tipo = request.form.get('tipo')
        qualidade = request.form.get('qualidade')
        descricao = request.form.get('descricao')
        endereco = request.form.get('endereco')
        login = session['login']

        if dao.inserir_roupas(tipo, qualidade, descricao, endereco, login):
            msg = 'roupa cadastrada com sucesso'
            return render_template('home.html', texto=msg)
        else:
            msg = 'Erro ao cadastrar roupa'
            return render_template('home.html', texto=msg)
    else:
        return render_template('index.html')
@app.route('/doar')
def doarroupa():
    if 'login' in session:
        return render_template('pagdoacao.html')
    else:
        return render_template('index.html')

@app.route('/listar')
def listarroupa():
    if 'login' in session:
        roupas = dao.listarroupa()
        return render_template('paglistarroupa.html', lista=roupas)
    else:
        return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
