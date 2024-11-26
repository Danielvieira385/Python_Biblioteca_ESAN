import diretorios as dir
import time
from datetime import datetime
import bcrypt

def validate_password(password):
    # Validação condicional da password
    if len(password) >= 4:
        return "A senha deve ter pelo maior ou igual que 4 caracteres."
    return True  # Retorna True se a password for válida

def record_user(nome, password):
    # Validação das condições iniciais
    if not nome:
        return "O nome não pode ser vazio."
    if not validate_password(password):
        return "Senha inválida."

    # Encriptação da password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Escreve no arquivo
    with open(dir.dirUsers, 'a') as user:
        user.write(f"{nome},{hashed_password}\n")
        print("Utilizador registado com sucesso!")
        countdown(3)

def countdown(t):
    for i in range(t, 0, -1):
        print(i)
        time.sleep(1)