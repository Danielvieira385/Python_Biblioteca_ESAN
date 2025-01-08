from smtplib import SMTP

# Função para enviar e-mail
def enviar_email(livro):
    
    utilizador = 'biblioteca.estarreja.py'
    senha = 'smbr riqh njiz gpmd'
    mensagem = f'Venho por este meio solicitar a devolucao do livro {livro}. \nObrigado.\n\nCumprimentos,\nBiblioteca de Estarreja'
    # destinatario = ['biblioteca.estarreja.py@gmail.com']
    destinatario = ['jssilva@ua.pt'] # Professor João Silva
    assunto = f'Devolucao do livro {livro}'
    
    
    smtp = SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(utilizador, senha)
    mensagem_completa = f'Subject: {assunto}\n\n{mensagem}'
    smtp.sendmail(utilizador, destinatario, mensagem_completa)
    smtp.quit()
    print('E-mail enviado com sucesso')
