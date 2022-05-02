import os
from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from models import *

app = Flask(__name__)

# MySQL configurations
#app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
#app.config['MYSQL_DATABASE_DB'] = 'ac'
#app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@172.17.0.2/ac'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def inicio():
    return render_template('aluno.html')

@app.route('/aluno', methods=['POST'])
def post_aluno():
    aluno = request.form.get('aluno')
    email = request.form.get('email')
    endereco = request.form.get('end')
    if aluno and email and endereco:
        alunos = Alunos(aluno, email, endereco)
        db.session.add(alunos)
        db.session.commit()
        db.session.flush()
        url = f"/lista/aluno/{alunos.id}"
        return redirect(url, code=302)
    return render_template('show_alunos.html')

@app.route('/lista/aluno/<int:nid>', methods=['GET'])
def show_aluno(nid):
    alunos = Alunos.query.filter_by(id=nid).all()
    db.session.commit()
    return render_template('show_alunos.html', alunos=alunos)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
