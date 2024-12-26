import csv
from datetime import datetime, timedelta
import diretorios as dir
import record_users_DB as users
import record_books_DB as books
import enviar_notificacao as email
import search_books as info_livro

# Função para registar o empréstimo dos livros
def registar_emprestimo(titulo, utilizador):
    # Define a data atual e a data de devolução
    data_atual = datetime.now().strftime('%Y-%m-%d')
    previsao_devolucao = data_devolucao(datetime.now())
        
    # Verifica se o utilizador está registado
    utilizador_encontrado = users.procurar_utilizador(utilizador)
    livro_encontrado = books.procura_livro(titulo)
    livro_emprestado = livro_disponivel(titulo)
    
    if utilizador_encontrado == True:
        if livro_encontrado == True:                              
            if livro_emprestado == True:
                # Indica que o livro já se encontra emprestado
                print(f"O livro '{titulo}' já se encontra emprestado.")
                print("Deseja ir para a fila de espera? (s/n): ")
                decisão = input().lower()
                # Adiciona o utilizador à fila de espera
                if decisão == "s":
                    with open(dir.dirFilaEspera, 'a', newline='') as fila_file:
                        info_livro_utilizador = csv.writer(fila_file)
                        info_livro_utilizador.writerow([titulo, utilizador])
                        print(f"O utilizador {utilizador} foi adicionado à fila de espera para o livro '{titulo}'.")
                        input("Pressione Enter para continuar...")
                        return                                
            if livro_emprestado == False:
                # Regista o empréstimo do livro
                with open(dir.dirEmprestimos, 'a', newline='') as emprestimos_file:
                    info_livro_utilizador = csv.writer(emprestimos_file)
                    info_livro_utilizador.writerow([titulo, utilizador, data_atual, previsao_devolucao.strftime('%Y-%m-%d'), ""])
                    print(f"O livro '{titulo}' foi emprestado ao utilizador {utilizador}.")
                    print("Data de devolução prevista:", previsao_devolucao.strftime('%Y-%m-%d'))
                # Regista o empréstimo para o histórico
                with open(dir.dirHistorico, 'a', newline='') as historico_file:
                    info_livro_utilizador = csv.writer(historico_file)
                    info_livro_utilizador.writerow([titulo, utilizador, data_atual])
                    input("Pressione Enter para continuar...")
                    return
        else:
            print(f"O livro '{titulo}' não foi encontrado.")
            input("Pressione Enter para continuar...")
    else:
        print(f"O utilizador {utilizador} não está registado.")
        input("Pressione Enter para continuar...")

# Função para registar o empréstimo dos livros com informações completas
def registar_emprestimo_completo(titulo, utilizador):
        
    # Verifica se o utilizador está registado
    utilizador_encontrado = users.procurar_utilizador(utilizador)
    livro_encontrado = books.procura_livro(titulo)
    livro_emprestado = livro_disponivel(titulo)
    detalhes_livro = info_livro.procurar_info_livro(titulo)
    
    # Informação do livro a ser emprestado
    autor = detalhes_livro[0]
    titulo = detalhes_livro[1]
    data_publicacao = detalhes_livro[2]
    genero = detalhes_livro[3]
    
    if utilizador_encontrado:
        if livro_encontrado:
            if livro_emprestado:
                print(f"O livro '{titulo}' já se encontra emprestado.")
                decisao = input("Deseja ir para a fila de espera? (s/n): ").lower()
                if decisao == "s":
                    with open(dir.dirFilaEspera, 'a', newline='') as fila_file:
                        info_livro_utilizador = csv.writer(fila_file)
                        info_livro_utilizador.writerow([titulo, utilizador])
                        print(f"O utilizador {utilizador} foi adicionado à fila de espera para o livro '{titulo}'.")
                        input("Pressione Enter para continuar...")
                        return
            else:
                data_atual = datetime.now().strftime('%Y-%m-%d')
                previsao_devolucao = data_devolucao(datetime.now())
                    
                    # Regista o empréstimo do livro
                with open(dir.dirEmprestimos, 'a', newline='') as emprestimos_file:
                    info_livro_utilizador = csv.writer(emprestimos_file)
                    info_livro_utilizador.writerow([titulo, autor, genero, data_publicacao, utilizador, data_atual, previsao_devolucao.strftime('%Y-%m-%d'), ""])
                    print(f"O livro '{titulo}' foi emprestado ao utilizador {utilizador}.")
                    print("Data de devolução prevista:", previsao_devolucao.strftime('%Y-%m-%d'))
                    
                    # Regista o empréstimo para o histórico
                with open(dir.dirHistorico, 'a', newline='') as historico_file:
                    info_livro_utilizador = csv.writer(historico_file)
                    info_livro_utilizador.writerow([titulo, autor, genero, data_publicacao, utilizador, data_atual, previsao_devolucao.strftime('%Y-%m-%d'), ""])
                    input("Pressione Enter para continuar...")
                    return
        else:
            print(f"O livro '{titulo}' não foi encontrado.")
            input("Pressione Enter para continuar...")
    else:
        print(f"O utilizador {utilizador} não está registado.")
        input("Pressione Enter para continuar...")

# Função para registar a devolução dos livros
def registar_devolucao(titulo):
    emprestimos = []
    devolvido = False

    # Carrega todos os empréstimos e marca o livro como devolvido
    with open(dir.dirEmprestimos, 'r', newline='') as emprestimos_file:
        lista_livros = csv.reader(emprestimos_file)
        for livro in lista_livros:
            if len(livro) == 8 and livro[0].strip() == titulo.strip() and livro[7] == "":
                livro[7] = datetime.now().strftime('%Y-%m-%d')  # Regista a data de devolução
                devolvido = True
            emprestimos.append(livro)

    if devolvido:
        # Atualiza o arquivo emprestimos_DB.csv com a devolução
        with open(dir.dirEmprestimos, 'w', newline='') as emprestimos_file:
            writer = csv.writer(emprestimos_file)
            writer.writerows(emprestimos)
        
        # Atualiza o arquivo historico_DB.csv com a devolução
        with open(dir.dirHistorico, 'w', newline='') as emprestimos_file:
            writer = csv.writer(emprestimos_file)
            writer.writerows(emprestimos)
            
        print(f"O livro '{titulo}' foi devolvido com sucesso.")
        input("Pressione Enter para continuar...")
    else:
        print(f"O livro '{titulo}' não foi encontrado na lista de empréstimos pendentes.")
        input("Pressione Enter para continuar...")

# Função para organizar a fila de espera
def filas_espera(titulo):
    fila_espera = []

    # Carrega a fila de espera
    with open(dir.dirFilaEspera, 'r') as file:
        lista_fila_espera = csv.reader(file)
        for livro in lista_fila_espera:
            if len(livro) == 2 and livro[0].strip() == titulo.strip():
                fila_espera.append(livro[1])  # Adiciona o nome do usuário à fila

    if not fila_espera:
        print(f"Não existe fila de espera para o livro '{titulo}'.")
        input("Pressione Enter para continuar...")
        return

    print(f"Fila de espera para o livro '{titulo}':")
    for i, utilizador in enumerate(fila_espera, 1):
        print(f"{i}. {utilizador}")

    
    devolver = input(f"Deseja notificar o primeiro utilizador da fila ({fila_espera[0]}) sobre a disponibilidade do livro? (s/n): ")
    if devolver.lower() == "s":
        # Envia um e-mail ao primeiro utilizador da fila
        email.enviar_email(titulo)
        print(f"Utilizador {fila_espera[0]} foi notificado.")
        input("Pressione Enter para continuar...")
    else:
        print("Fila de espera não foi alterada.")
        input("Pressione Enter para continuar...")

# Função para calcular em dias úteis a data de devolução
def data_devolucao(data_inicial):
    dias_adicionados = 0
    data_final = data_inicial
    while dias_adicionados < 10:
        data_final += timedelta(days=1)
        if data_final.weekday() < 5:
            dias_adicionados += 1
    return data_final

# Função disponibilidade do livro
def livro_disponivel(titulo):
    emprestado = False
    with open(dir.dirEmprestimos, 'r') as file:
        lista_emprestimos = csv.reader(file)
        for livro in lista_emprestimos:
            if len(livro) == 5 and livro[0].strip() == titulo.strip() and livro[4] == "":
                emprestado = True
                break
    if emprestado:
        return True
    else:
        return False
    
   