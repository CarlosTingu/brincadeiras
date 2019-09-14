# -*- coding: utf-8 -*-

#Importando modulos
import sqlite3

#Fazendo conexão com o banco de dados
conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

#Inserindo códigos SQL no banco de dados
cursor.execute("""
CREATE TABLE usuarios (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
idade INTEGER,
cpf VARCHAR(11) NOT NULL,
email TEXT NOT NULL,
fone TEXT,
cidade TEXT,
criado_em DATE NOT NULL);""")

print('Tabela criada com sucesso!')

#Feachando conexão
conn.close()
