import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s %(levelname)s:%(message)s')

def enviar_email(destinatario, assunto, mensagem):
    remetente = 'biblioteca.estarreja.py@gmail.com'
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "biblioteca.estarreja.py@gmail.com"
    password = os.getenv('EMAIL_PASSWORD')  # Use environment variable for password

    # Create a secure SSL context
    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)  # Secure the connection
        server.login(sender_email, password)
        msg = MIMEMultipart()
        msg['From'] = remetente
        msg['To'] = destinatario
        msg['Subject'] = assunto
        msg.attach(MIMEText(mensagem, 'plain'))
        server.sendmail(sender_email, destinatario, msg.as_string())
    except Exception as event:
        logging.error(f"Erro ao enviar email: {event}")
    finally:
        server.quit()

if __name__ == "__main__":
    # Exemplo de uso
    destinatario = 'biblioteca.estarreja.py@gmail.com'
    assunto = 'Assunto do Email'
    mensagem = 'Corpo do email'
    enviar_email(destinatario, assunto, mensagem)