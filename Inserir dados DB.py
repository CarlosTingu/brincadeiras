# -*- coding: utf-8 -*-

#importando modulo DB
import sqlite3

#Fazendo conexão com o banco de dados
conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

#Solicitando os dados ao usuário
nome = raw_input('Nome: ')
idade = raw_input('Idade: ')
cpf = raw_input('CPF: ')
email = raw_input('Email: ')
fone = raw_input('Fone: ')
cidade = raw_input('Cidade: ')
criado_em = raw_input('Criado em (dd-mm-yyyy): ')

#Inserindo códigos SQL no banco de dados
cursor.execute("""
INSERT INTO usuarios (nome, idade, cpf, email, fone, cidade, criado_em)
VALUES (?,?,?,?,?,?,?)
""", (nome, idade, cpf, email, fone, cidade, criado_em))

conn.commit()

print('Dados inseridos com sucesso!')

#Fechando conexão
conn.close()
