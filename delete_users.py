import diretorios as dirs

# Remove um utilizador do arquivo de utilizadores
def remove_user(utilizador=None, id_usuario=None):
    # Validação inicial
    if not utilizador and not id_usuario:
        return "É necessário fornecer o nome do utilizador ou o ID do utilizador."
    # Inicia o dicionário de usuários
    usuarios = {}
    # Verifica se o arquivo existe
    with open(dirs.dirUsers, 'r') as arquivo:
        for linha in arquivo:
            id_usuario_arquivo, nome_usuario = linha.strip().split(":", 1)
            usuarios[int(id_usuario_arquivo)] = nome_usuario
    # Verificar se o utilizador está registado
    usuario_encontrado = False
    if utilizador:
        for id_usuario_arquivo, nome_usuario in usuarios.items():
            if nome_usuario == utilizador:
                del usuarios[id_usuario_arquivo]  # Remove o usuário encontrado
                usuario_encontrado = True
                confirm = input(f"Tem certeza que deseja remover o utilizador {utilizador}? (s/n): ")
                if confirm.lower() == 's':
                    break
                else:
                    return "Remoção cancelada."
    elif id_usuario:
        if int(id_usuario) in usuarios:
            print(f"Utilizador encontrado: {id_usuario}:{usuarios[int(id_usuario)]}")
            confirm = input(f"Tem certeza que deseja remover o utilizador {usuarios[int(id_usuario)]}? (s/n): ")
            if confirm.lower() == 's':
                del usuarios[int(id_usuario)]  # Remove o usuário encontrado
                usuario_encontrado = True
            else:
                return "Remoção cancelada."

    if not usuario_encontrado:
        print("Esse utilizador não foi encontrado.")
        input("Pressione Enter para continuar...")
        return "Esse utilizador não foi encontrado."
    # Salvar o dicionário atualizado no arquivo
    with open(dirs.dirUsers, 'w') as arquivo:
        for id_usuario_arquivo, nome_usuario in usuarios.items():
            arquivo.write(f"{id_usuario_arquivo}:{nome_usuario}\n")
    
    print("Utilizador removido com sucesso!")
    input("Pressione Enter para continuar...")
    return "Remoção concluída."
