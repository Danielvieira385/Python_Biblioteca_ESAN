import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

def enviar_email(destinatarios, assunto, mensagem):
    remetente = 'biblioteca.estarreja.py@gmail.com'
    smtp_server = "smtp.gmail.com"
    port = 587 
    sender_email = "biblioteca.estarreja.py@gmail.com"
    password = '.123456789.'
    
    # Create a secure SSL context
    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)  # Secure the connection
        server.login(sender_email, password)
        msg = MIMEMultipart()
        msg['From'] = remetente
        msg['To'] = ", ".join(destinatarios)
        msg['Subject'] = assunto
        msg.attach(MIMEText(mensagem, 'plain'))
        server.sendmail(sender_email, destinatarios, msg.as_string())
    except (smtplib.SMTPException, ssl.SSLError) as event:
        logging.error(f"Erro ao enviar email para {destinatarios}: {event}")
    finally:
        server.quit()

if __name__ == "__main__":
    # Exemplo de uso
    # Example usage for testing purposes only. Do not use hardcoded credentials in production.
    destinatarios = ['biblioteca.estarreja.py@gmail.com']
    assunto = 'Assunto do Email'
    mensagem = 'Corpo do email'
    enviar_email(destinatarios, assunto, mensagem)