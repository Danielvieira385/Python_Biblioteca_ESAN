import csv
from datetime import datetime
import os

#caminho relativo do ficheiro
current_dir = os.path.dirname(__file__)
dirBooks = os.path.join(current_dir, 'books_DB.csv')

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
        #modificacao para a data nao ser superior ao ano atual
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

def get_all_books():
    books = []
    with open(dirBooks, 'r') as file:
        lista = csv.reader(file)
        for row in lista:
            if len(row) == 3:  # Certifique-se de que a linha tem 4 elementos
                book = {
                    'autor': row[0],
                    'title_book': row[1],
                    'genero_book': row[2],
                    # 'publish_date': row[3]
                }
                books.append(book)
    return books





