import diretorios as dir
import time
from datetime import datetime

def recordUser(nome, password):
    user_info = []

    # Verifica se o nome é uma string não vazia
    if isinstance(nome, str) and nome:
        user_info.append(nome)
    else:
        print("O nome não deve ser um campo em vazio.")

    # Verifica se password é uma string não vazia
    if isinstance(password, str) and password:
        user_info.append(password)
    else:
        print("A password não deve ser um campo em vazio.")

    user_info_str = ",".join(user_info)

    with open(dir.dirUsers, 'a') as user:
        user.write(user_info_str + "\n")
        print("Utilizador registado com sucesso!")
        print("Voltar ao Menu em ...")
        
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)

        # time.sleep(3) # delay de 3 segundos até desaparecer a mensagem
