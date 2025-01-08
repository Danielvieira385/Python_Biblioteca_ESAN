import csv
import time
from datetime import datetime
import diretorios as dir

# Função para registar um livro na base de dados
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

    with open(dir.dirBooks, 'a') as book:
        book.write(book_info_str + "\n")
        print("Livro inserido na base dados com sucesso!")

#dicionario para a pesquisa.
def get_all_books():
    books = []
    try:
        with open(dir.dirBooks, 'r') as file:
            lista = csv.DictReader(file, fieldnames=['autor', 'title_book', 'publish_date', 'genero_book'])
            for row in lista:
                if len(row) == 4:  #tem de ter 4

                    books.append(row)
    except FileNotFoundError:
        print(f"Erro: O arquivo {dir.dirBooks} não foi encontrado. Verifique se o caminho está correto.")
        return []
    return books

# Função para listar todos os livros na base de dados
def remover_livro(titulo):
    livros = []
    livro_removido = False
    
    # Ler todos os livros e armazená-los numa lista, exceto o livro a ser removido
    try:
        with open(dir.dirBooks, 'r', newline='') as file:
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
        with open(dir.dirBooks, 'w', newline='') as file:
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

# Função para atualizar as informações de um livro na base de dados
def atualizar_informacoes_livro(titulo):
    livros = []
    livro_atualizado = False
    
    # Ler todos os livros e armazená-los numa lista
    try:
        with open(dir.dirBooks, 'r', newline='') as file:
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
        with open(dir.dirBooks, 'w', newline='') as file:
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

# Função para procurar um livro pelo título        
def procura_livro(titulo):
    livros = []
   
    with open(dir.dirBooks, 'r', newline='') as file:
        lista_livros = csv.reader(file)
        for livro in lista_livros:
            if len(livro) == 4:  
                titulo_no_csv = livro[1].strip()
                if titulo_no_csv == titulo.strip():
                    livros.append(livro)
                    break
    if livros:
        return True
    else:
        return False