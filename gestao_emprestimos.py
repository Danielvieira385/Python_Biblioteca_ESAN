import csv
from datetime import datetime
import diretorios as dir

def registar_emprestimo(titulo, utilizador):
    livro_encontrado = False
    # Carrega a lista de livros para verificar disponibilidade
    with open(dir.dirBooks, 'r') as file:
        lista_livros = csv.reader(file)
        for livro in lista_livros:
            if len(livro) == 4 and livro[1].strip() == titulo.strip():
                livro_encontrado = True
                break
    if not livro_encontrado:
        print(f"O livro '{titulo}' não está disponível na biblioteca.")
        return
    
    # Verifica se o livro já está emprestado e adiciona à fila de espera
    with open(dir.dirEmprestimos, 'r') as file:
        lista_emprestimos = csv.reader(file)
        for livro in lista_emprestimos:
            if len(livro) == 4 and livro[0].strip() == titulo.strip() and livro[3] == "":
                print(f"O livro '{titulo}' já se encontra emprestado. Você foi adicionado à fila de espera.")
                # Adiciona o utilizador à fila de espera
                with open(dir.dirFilaEspera, 'a', newline='') as fila_file:
                    info_livro_utilizador = csv.writer(fila_file)
                    info_livro_utilizador.writerow([titulo, utilizador])
                return
    
    # Regista o empréstimo do livro
    with open(dir.dirEmprestimos, 'a', newline='') as emprestimos_file:
        info_livro_utilizador = csv.writer(emprestimos_file)
        info_livro_utilizador.writerow([titulo, utilizador, datetime.now().strftime('%Y-%m-%d'), ""])
    print(f"O livro '{titulo}' foi emprestado ao usuário {utilizador}.")
    
    # Regista o empréstimo para o histórico
    with open(dir.dirHistorico, 'a', newline='') as historico_file:
        info_livro_utilizador = csv.writer(historico_file)
        info_livro_utilizador.writerow([titulo, utilizador, datetime.now().strftime('%Y-%m-%d'), ""])

def registar_devolucao(titulo):
    emprestimos = []
    devolvido = False

    # Carrega todos os empréstimos e marca o livro como devolvido
    with open(dir.dirEmprestimos, 'r', newline='') as emprestimos_file:
        lista_livros = csv.reader(emprestimos_file)
        for livro in lista_livros:
            if len(livro) == 4 and livro[0].strip() == titulo.strip() and livro[3] == "":
                livro[3] = datetime.now().strftime('%Y-%m-%d')  # Registrar a data de devolução
                devolvido = True
            emprestimos.append(livro)

    if devolvido:
        # Atualizar o arquivo emprestimos_DB.csv com a devolução
        with open(dir.dirEmprestimos, 'w', newline='') as emprestimos_file:
            writer = csv.writer(emprestimos_file)
            writer.writerows(emprestimos)
        print(f"O livro '{titulo}' foi devolvido com sucesso.")
    else:
        print(f"O livro '{titulo}' não foi encontrado na lista de empréstimos pendentes.")

def organizar_fila_espera(titulo):
    fila_espera = []

    # Carregar a fila de espera
    with open(dir.dirFilaEspera, 'r') as file:
        lista_fila = csv.reader(file)
        for livro in lista_fila:
            if len(livro) == 2 and livro[0].strip() == titulo.strip():
                fila_espera.append(livro[1])  # Adiciona o nome do usuário à fila

    if not fila_espera:
        print(f"Não há ninguém na fila de espera para o livro '{titulo}'.")
        return

    print(f"Organizando fila de espera para o livro '{titulo}':")
    for i, utilizador in enumerate(fila_espera, 1):
        print(f"{i}. {utilizador}")

    # Opcional: Podemos remover o primeiro usuário da fila quando o livro for devolvido
    devolver = input(f"Deseja notificar o primeiro usuário da fila ({fila_espera[0]}) sobre a disponibilidade do livro? (s/n): ")
    if devolver.lower() == "s":
        # Retirar o primeiro da fila de espera
        fila_espera.pop(0)

        # Atualizar a fila de espera no arquivo
        with open(dir.dirFilaEspera, 'w', newline='') as file:
            writer = csv.writer(file)
            for utilizador in fila_espera:
                writer.writerow([titulo, utilizador])
        
        print(f"Usuário {fila_espera[0]} foi notificado.")
    else:
        print("Fila de espera não foi alterada.")