# -*- coding: utf-8 -*-

import smtplib

smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)

print("#####################################")
print("#####################################")
print("########ENVIAR EMAIL By:TINGU########")
print("#####################################")
print("#####################################")

login_email = str(input('MEU E-MAIL: '))
login_senha = str(input('MINHA SENHA: '))

try:
    smtp.login(login_email, login_senha)
    print('CONECTADO COM SUCESSO')
except:
    print('USUÁRIO INVÁLIDO')
    exit()    
    
msg_assunto = str(input('ASSUNTO: '))
msg_texto = str(input('MENSAGEM DE TEXTO: '))
msg_de = login_email
msg_para = str(input('ENVIAR PARA => '))
msg = """From: %s
To: %s
Subject: %s 

%s"""%(msg_de, msg_para, msg_assunto, msg_texto) 

try:
    smtp.sendmail(msg_de, msg_para, msg)
    print('E-MAIL ENVIADO COM SUCESSO')
except:
    print('E-MAIL NÃO ENVIADO')
    
smtp.quit()
