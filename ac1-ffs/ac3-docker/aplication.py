import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)

from models import *

@app.route('/')
def main():
    return render_template('cadastro.html')

@app.route('/cadastro/produto', methods=['POST'])
def cadastro():
    produto = request.form['name']
    categoria = request.form['categoria']
    valor = request.form['valor']
    produtos = Produtos(produto, categoria, valor)
    db.session.add(produtos)
    db.session.commit()
    db.session.flush()
    url = f"/lista/produto/{produtos.id}"
    return redirect(url, code=302)

@app.route('/lista/produto/<int:nid>', methods=['GET'])
def listagem(nid):
    data = Produtos.query.filter_by(id=nid).all()
    db.session.commit()
    return render_template('lista.html', data=data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(host='0.0.0.0', port=port)