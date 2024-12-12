import diretorios as dir

# Função para registar um novo utilizador
def record_user(utilizador):
    # Validação inicial
    if not utilizador.strip():
        return "O utilizador não pode ser vazio."   
    
    usuarios = procurar_utilizador(utilizador) 
     
    if usuarios == True:
        print("O utilizador já existe.")
        input("Pressione Enter para continuar...")
        return
    else:
        # Inicia o dicionário de usuários
        novo_usuarios = {}
        
        # Importa a lista de utilizadores
        with open(dir.dirUsers, 'r') as lista_users:
            for linha in lista_users:
                id_usuario, nome_usuario = linha.strip().split(":", 1)
                novo_usuarios[int(id_usuario)] = nome_usuario

        # Cria um ID para o novo utilizador e adiciona ao dicionário
        novo_id = max(novo_usuarios.keys(), default=0) + 1
        novo_usuarios[novo_id] = utilizador

        # Exporta o dicionário atualizado para a base dados
        with open(dir.dirUsers, 'w') as lista_users:
            for id_usuario, nome_usuario in novo_usuarios.items():
                lista_users.write(f"{id_usuario}:{nome_usuario}\n")
        print("Utilizador registado com sucesso!")
        print(f"ID de utilizador: {novo_id}: {utilizador}")
        input("Pressione Enter para continuar...")
        return
    
# Função para verificar se um utilizador está registado
def procurar_utilizador(utilizador):
    # Inicia o dicionário de usuários
    usuarios = {}
    with open(dir.dirUsers, 'r') as lista_users:
        for linha in lista_users:
            id_usuario, nome_usuario = linha.strip().split(":", 1)
            usuarios[int(id_usuario)] = nome_usuario
         
    # Verifica se o utilizador está registado
    if utilizador in usuarios.values():
        return True
    else:
        return False