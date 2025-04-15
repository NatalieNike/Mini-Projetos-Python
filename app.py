#API é um lugar para disponibilizar recursos e/ou funcionalidades
#1. Objetivo - Criar um api que disponibiliza a conslta, criação, edição e exclusão de livros.
#2. URL base - localhost.com
#3. Endpoints - (localhost/livros - GET), (localhost/livros - POST), (localhost/livros/id - GET), (localhost/livros/id - PUT), (localhost/livros/id - DELETE)
#4. Quais recursos - 

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O Senhor do Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 3,
        'título': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K. Rowlling'
    },
    {
        'id': 3,
        'título': 'Hábitos Atomicos',
        'autor': 'James Clear'
    },
]
# Vamos:
# Consultar(todos)
# Consultar(id)
# Editar
# Excluir
