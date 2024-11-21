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

    # Verifica se o genero é uma string não vazia
    if isinstance(genero_book, str) and genero_book:
        book_info.append(genero_book)
    else:
        print("O género da obra não deve ser um campo em vazio.")

    # Tenta converter a data de publicação para um inteiro e verifica se é positiva
    try:
        publish_date = int(publish_date)
        current_year = datetime.now().year
        if publish_date > 0 and publish_date <= current_year:
            book_info.append(str(publish_date))
        elif publish_date > current_year:
            print("O ano de publicação não pode ser superior ao ano atual.")
        else:
            print("O ano de publicação deve conter 4 digítos.")
    except ValueError:
        print("O ano de publicação deve ser um número inteiro.")

    book_info_str = ",".join(book_info)

    with open(dirBooks, 'a') as book:
        book.write(book_info_str + "\n")
        print("Livro inserido na base dados com sucesso!")

# Le todos os livros do csv e retorna uma lista de dicionários
def get_all_books():
    books = []
    with open(dirBooks, 'r') as file:
        lista = csv.DictReader(file, fieldnames=['autor', 'title_book', 'genero_book', 'publish_date'])
        for row in lista:
            books.append(row)
    return books





