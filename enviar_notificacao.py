from smtplib import SMTP

# Função para enviar e-mail
def enviar_email(usuario,senha,mensagem,listadestinatarios):
    smtp = SMTP('smtp.gmail.com',587)
    smtp.starttls()
    smtp.login(usuario,senha)
    smtp.sendmail(usuario,listadestinatarios,mensagem)
    smtp.quit()
    print('E-mail enviado com sucesso')
enviar_email('biblioteca.estarreja.py','.123456789.','ola mundo',['biblioteca.estarreja.py@gmail.com'])
 
 
 