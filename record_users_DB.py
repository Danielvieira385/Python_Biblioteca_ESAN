import diretorios as dir

def record_user(utilizador):
    # Validação inicial
    if not utilizador.strip():
        return "O utilizador não pode ser vazio."
    # Inicia o dicionário de usuários
    usuarios = {}

    with open(dir.dirUsers, 'r') as arquivo:
        for linha in arquivo:
            id_usuario, nome_usuario = linha.strip().split(":", 1)
            usuarios[int(id_usuario)] = nome_usuario

    # Verificar se o utilizador já está registado
    if utilizador in usuarios.values():
        print("Esse utilizador já existe.")
        input("Pressione Enter para continuar...")
        return "Esse utilizador já existe."

    # Gerar um ID para o novo usuário e adiciona ao dicionário
    novo_id = max(usuarios.keys(), default=0) + 1
    usuarios[novo_id] = utilizador

    # Salvar o dicionário atualizado no arquivo
    with open(dir.dirUsers, 'w') as arquivo:
        for id_usuario, nome_usuario in usuarios.items():
            arquivo.write(f"{id_usuario}:{nome_usuario}\n")
    print("Utilizador registado com sucesso!")
    print(f"ID de utilizador: {novo_id}: {utilizador}")
    input("Pressione Enter para continuar...")

    return "Registo concluído."
