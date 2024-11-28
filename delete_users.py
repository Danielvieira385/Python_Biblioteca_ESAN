import os
import time
import diretorios as dirs

def remove_user(utilizador):

    # Validação inicial
    if not utilizador.strip():
        return "O utilizador não pode ser vazio."

    # Inicia o dicionário de usuários
    usuarios = {}

    # Verifica se o arquivo existe
    with open(dirs.dirUsers, 'r') as arquivo:
        for linha in arquivo:
            id_usuario, nome_usuario = linha.strip().split(":", 1)
            usuarios[int(id_usuario)] = nome_usuario

    # Verificar se o utilizador está registado
    usuario_encontrado = False
    for id_usuario, nome_usuario in usuarios.items():
        if nome_usuario == utilizador:
            del usuarios[id_usuario]  # Remove o usuário encontrado
            usuario_encontrado = True
            break

    if not usuario_encontrado:
        print("Esse utilizador não foi encontrado.")
        countdown(3)
        return "Esse utilizador não foi encontrado."

    # Salvar o dicionário atualizado no arquivo
    with open(dirs.dirUsers, 'w') as arquivo:
        for id_usuario, nome_usuario in usuarios.items():
            arquivo.write(f"{id_usuario}:{nome_usuario}\n")
    
    print("Utilizador removido com sucesso!")
    countdown(3)
    return "Remoção concluída."

def countdown(t):
    for i in range(t, 0, -1):
        print(i)
        time.sleep(1)