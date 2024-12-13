import smtplib, ssl 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

### Ainda em desenvolvimento ###

def enviar_email(destinatario, assunto, mensagem):
    remetente = 'biblioteca.estarreja.py@gmail.com'
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "biblioteca.estarreja.py@gmail.com"
    password = '.123456789.'

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        msg = MIMEMultipart()
        msg['From'] = remetente
        msg['To'] = destinatario
        msg['Subject'] = assunto
        msg.attach(MIMEText(mensagem, 'plain'))
        server.sendmail(remetente, destinatario, msg.as_string())
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()

# Exemplo de uso
destinatario = 'biblioteca.estarreja.py@gmail.com'
assunto = 'Assunto do Email'
mensagem = 'Corpo do email'
enviar_email(destinatario, assunto, mensagem)