import csv
from datetime import datetime
import diretorios as dir

def registrar_emprestimo(titulo, usuario):
    livro_encontrado = False

    # Carregar a lista de livros para verificar disponibilidade
    with open(dir.dirBooks, 'r') as file:
        lista = csv.reader(file)
        for row in lista:
            if len(row) == 4 and row[1].strip() == titulo.strip():
                livro_encontrado = True
                break

    if not livro_encontrado:
        print(f"O livro '{titulo}' não está disponível na biblioteca.")
        return

    # Verificar se o livro já está emprestado e adicionar à fila de espera
    with open(dir.dirEmprestimos, 'r') as file:
        lista_emprestimos = csv.reader(file)
        for row in lista_emprestimos:
            if len(row) == 4 and row[0].strip() == titulo.strip() and row[3] == "":
                print(f"O livro '{titulo}' já está emprestado. Você foi adicionado à fila de espera.")
                # Adicionar à fila de espera
                with open(dir.dirFilaEspera, 'a', newline='') as fila_file:
                    writer = csv.writer(fila_file)
                    writer.writerow([titulo, usuario])
                return

    # Registrar o empréstimo caso o livro não tenha sido emprestado
    with open(dir.dirEmprestimos, 'a', newline='') as emprestimos_file:
        writer = csv.writer(emprestimos_file)
        writer.writerow([titulo, usuario, datetime.now().strftime('%Y-%m-%d'), ""])
    print(f"O livro '{titulo}' foi emprestado ao usuário {usuario}.")

def registrar_devolucao(titulo):
    emprestimos = []
    devolvido = False

    # Carregar todos os empréstimos e marcar o livro como devolvido
    with open(dir.dirEmprestimos, 'r', newline='') as emprestimos_file:
        lista = csv.reader(emprestimos_file)
        for row in lista:
            if len(row) == 4 and row[0].strip() == titulo.strip() and row[3] == "":
                row[3] = datetime.now().strftime('%Y-%m-%d')  # Registrar a data de devolução
                devolvido = True
            emprestimos.append(row)

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
        for row in lista_fila:
            if len(row) == 2 and row[0].strip() == titulo.strip():
                fila_espera.append(row[1])  # Adiciona o nome do usuário à fila

    if not fila_espera:
        print(f"Não há ninguém na fila de espera para o livro '{titulo}'.")
        return

    print(f"Organizando fila de espera para o livro '{titulo}':")
    for i, usuario in enumerate(fila_espera, 1):
        print(f"{i}. {usuario}")

    # Opcional: Podemos remover o primeiro usuário da fila quando o livro for devolvido
    devolver = input(f"Deseja notificar o primeiro usuário da fila ({fila_espera[0]}) sobre a disponibilidade do livro? (S/N): ")
    if devolver.upper() == "S":
        # Retirar o primeiro da fila de espera
        fila_espera.pop(0)

        # Atualizar a fila de espera no arquivo
        with open(dir.dirFilaEspera, 'w', newline='') as file:
            writer = csv.writer(file)
            for usuario in fila_espera:
                writer.writerow([titulo, usuario])
        
        print(f"Usuário {fila_espera[0]} foi notificado.")
    else:
        print("Fila de espera não foi alterada.")