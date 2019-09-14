# -*- coding: utf-8 -*-

#Importando modulo
import sqlite3

#Fazendo conexão com o DB
conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

#Lendo os dados do DB
cursor.execute(""" SELECT * FROM usuarios """)

#Lendo dados do cursor
for linha in cursor.fetchall():
    print(linha)

#Fechando conexão
conn.close()
