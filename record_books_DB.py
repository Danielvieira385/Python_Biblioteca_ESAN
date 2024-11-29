import csv
from datetime import datetime

dirBooks = "C:\\Users\\Toni\\OneDrive - Universidade de Aveiro\\Projeto Python\\BibliotecaESAN\\books_DB.csv"

def recordBook(autor, title_book, genero_book, publish_date):
    book_info = []

    # Verifica se o autor é uma string não vazia
    if isinstance(autor, str) and autor:
        book_info.append(autor)
    else:
        print("O nome do autor não deve ser um campo em vazio.")

    # Verifica se o título é uma string não vazia
    if isinstance(title_book, str) and title_book:
        book_info.append(title_book)
    else:
        print("O título da obra não deve ser um campo em vazio.")

    # Verifica se o gênero é uma string não vazia
    if isinstance(genero_book, str) and genero_book:
        book_info.append(genero_book)
    else:
        print("O gênero da obra não deve ser um campo em vazio.")

    # Tenta converter a data de publicação para um inteiro e verifica se é válida
    try:
        publish_date = int(publish_date)
        current_year = datetime.now().year
        if 1000 <= publish_date <= current_year:
            book_info.append(str(publish_date))
        elif publish_date > current_year:
            print("O ano de publicação não pode ser superior ao ano atual.")
        else:
            print("O ano de publicação deve ter 4 dígitos e ser positivo.")
    except ValueError:
        print("O ano de publicação deve ser um número inteiro.")

    book_info_str = ",".join(book_info)

    with open(dirBooks, 'a') as book:
        book.write(book_info_str + "\n")
        print("Livro inserido na base dados com sucesso!")


#dicionario para a pesquisa.
def get_all_books():
    books = []
    with open(dirBooks, 'r') as file:
        lista = csv.DictReader(file, fieldnames=['autor', 'title_book', 'genero_book', 'publish_date'])
        for row in lista:
            if len(row) == 4:  # mudar para 4 quando genero funcionar
                book = {
                    'autor': row[0],
                    'title_book': row[1],
                    'genero_book': row[2],
                    'publish_date': row[3]
                }
                books.append(book)
    return books


def remover_livro(titulo):
    livros = []
    livro_removido = False
    
    # Ler todos os livros e armazená-los numa lista, exceto o livro a ser removido
    try:
        with open(dirBooks, 'r', newline='') as file:
            lista = csv.reader(file)
            for row in lista:
                if len(row) == 3:  # Verifica se a linha tem o formato esperado (autor, título, ano)
                    # Reconstrói o título para comparação exata, caso ele contenha vírgulas
                    titulo_no_csv = row[1].strip()
                    if titulo_no_csv != titulo.strip():
                        livros.append(row)
                    else:
                        livro_removido = True

    except FileNotFoundError:
        print("O arquivo 'books_DB.csv' não foi encontrado.")
        return

    # Escrever a lista atualizada de livros de volta no CSV
    if livro_removido:
        with open(dirBooks, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(livros)
        mensagem = f"O livro '{titulo}' foi removido com sucesso."
        for char in mensagem:
            print(char, end="", flush=True)
            time.sleep(0.05)
        print("\n")
    else:
        mensagem = f"O livro '{titulo}' não foi encontrado."
        for char in mensagem:
            print(char, end="", flush=True)
            time.sleep(0.05)
        print("\n")

def atualizar_informacoes_livro(titulo):
    livros = []
    livro_atualizado = False
    
    # Ler todos os livros e armazená-los numa lista
    try:
        with open(dirBooks, 'r', newline='') as file:
            lista = csv.reader(file)
            for row in lista:
                if len(row) == 3:  # Verifica se a linha tem o formato esperado (autor, título, ano)
                    # Reconstrói o título para comparação exata, caso ele contenha vírgulas
                    titulo_no_csv = row[1].strip()
                    if titulo_no_csv == titulo.strip():
                        print(f"\nLivro encontrado: {row}")
                        
                        # Solicitar novas informações ao utilizador
                        novo_autor = input("Indique o novo nome do autor (deixe em branco para manter o atual): ") or row[0]
                        novo_titulo = input("Indique o novo título da obra (deixe em branco para manter o atual): ") or row[1]
                        try:
                            novo_ano = int(input("Indique o novo ano de publicação (deixe em branco para manter o atual): ") or row[2])
                        except ValueError:
                            print("O ano de publicação deve ser um número inteiro. Mantendo o valor atual.")
                            novo_ano = row[2]

                        # Substituir as informações antigas pelas novas
                        livros.append([novo_autor, novo_titulo, str(novo_ano)])
                        livro_atualizado = True
                    else:
                        livros.append(row)

    except FileNotFoundError:
        print("O arquivo 'books_DB.csv' não foi encontrado.")
        return

    # Escrever a lista atualizada de livros de volta no CSV
    if livro_atualizado:
        with open(dirBooks, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(livros)
        mensagem = "O livro '{titulo}' foi atualizado com sucesso."
        for char in mensagem:
            print(char, end="", flush=True)
            time.sleep(0.05)
        print("\n")
    else:
        mensagem = "O livro '{titulo}' não foi encontrado."
        for char in mensagem:
            print(char, end="", flush=True)
            time.sleep(0.05)
        print("\n")


def registrar_emprestimo(titulo, usuario):
    livro_encontrado = False

    # Carregar a lista de livros para verificar disponibilidade
    with open(dirBooks, 'r') as file:
        lista = csv.reader(file)
        for row in lista:
            if len(row) == 4 and row[1].strip() == titulo.strip():
                livro_encontrado = True
                break

    if not livro_encontrado:
        print(f"O livro '{titulo}' não está disponível na biblioteca.")
        return

    # Verificar se o livro já está emprestado e adicionar à fila de espera
    with open(dirEmprestimos, 'r') as file:
        lista_emprestimos = csv.reader(file)
        for row in lista_emprestimos:
            if len(row) == 4 and row[0].strip() == titulo.strip() and row[3] == "":
                print(f"O livro '{titulo}' já está emprestado. Você foi adicionado à fila de espera.")
                # Adicionar à fila de espera
                with open(dirFilaEspera, 'a', newline='') as fila_file:
                    writer = csv.writer(fila_file)
                    writer.writerow([titulo, usuario])
                return

    # Registrar o empréstimo caso o livro não tenha sido emprestado
    with open(dirEmprestimos, 'a', newline='') as emprestimos_file:
        writer = csv.writer(emprestimos_file)
        writer.writerow([titulo, usuario, datetime.now().strftime('%Y-%m-%d'), ""])
    print(f"O livro '{titulo}' foi emprestado ao usuário {usuario}.")

def registrar_devolucao(titulo):
    emprestimos = []
    devolvido = False

    # Carregar todos os empréstimos e marcar o livro como devolvido
    with open(dirEmprestimos, 'r', newline='') as emprestimos_file:
        lista = csv.reader(emprestimos_file)
        for row in lista:
            if len(row) == 4 and row[0].strip() == titulo.strip() and row[3] == "":
                row[3] = datetime.now().strftime('%Y-%m-%d')  # Registrar a data de devolução
                devolvido = True
            emprestimos.append(row)

    if devolvido:
        # Atualizar o arquivo emprestimos_DB.csv com a devolução
        with open(dirEmprestimos, 'w', newline='') as emprestimos_file:
            writer = csv.writer(emprestimos_file)
            writer.writerows(emprestimos)
        print(f"O livro '{titulo}' foi devolvido com sucesso.")
    else:
        print(f"O livro '{titulo}' não foi encontrado na lista de empréstimos pendentes.")


def organizar_fila_espera(titulo):
    fila_espera = []

    # Carregar a fila de espera
    with open(dirFilaEspera, 'r') as file:
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
        with open(dirFilaEspera, 'w', newline='') as file:
            writer = csv.writer(file)
            for usuario in fila_espera:
                writer.writerow([titulo, usuario])
        
        print(f"Usuário {fila_espera[0]} foi notificado.")
    else:
        print("Fila de espera não foi alterada.")