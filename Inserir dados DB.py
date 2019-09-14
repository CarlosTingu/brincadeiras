# -*- coding: utf-8 -*-

#importando modulo DB
import sqlite3

#Fazendo conexão com o banco de dados
conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

#Solicitando os dados ao usuário
p_nome = raw_input('Nome: ')
p_idade = raw_input('Idade: ')
p_cpf = raw_input('CPF: ')
p_email = raw_input('Email: ')
p_fone = raw_input('Fone: ')
p_cidade = raw_input('Cidade: ')
p_criado_em = raw_input('Criado em (dd-mm-yyyy): ')

#Inserindo códigos SQL no banco de dados
cursor.execute("""
INSERT INTO usuarios (nome, idade, cpf, email, fone, cidade, criado_em)
VALUES (?,?,?,?,?,?,?)
""", (p_nome, p_idade, p_cpf, p_email, p_fone, p_cidade, p_criado_em))

conn.commit()

print('Dados inseridos com sucesso!')

#Fechando conexão
conn.close()
