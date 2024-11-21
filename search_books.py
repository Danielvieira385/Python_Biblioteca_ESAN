import record_books_DB as rb
import csv

# Filtra a lista de livros pelo título fornecido, seja em maiúsculas ou minúsculas
def search_by_title(title):
    books = rb.get_all_books()
    matching_books = [book for book in books if title.lower() in book['title_book'].lower()]
    return matching_books

# Filtra a lista de livros pelo autor fornecido, seja em maiúsculas ou minúsculas
def search_by_author(author):
    books = rb.get_all_books()
    return [book for book in books if book['autor'] and author.lower() in book['autor'].lower()]

def filter_books(criteria):
    # Chama a função get_all_books() que coloquei no módulo record_books_DB.py
    books = rb.get_all_books()
    # Inicia a lista de livros filtrados com todos os livros
    filtered_books = books
    # Filtra a lista de livros para incluir apenas com aquele título
    if 'title' in criteria:
        filtered_books = [book for book in filtered_books if book['title_book'] and criteria['title'].lower() in book['title_book'].lower()]
    if 'author' in criteria:
        filtered_books = [book for book in filtered_books if book['autor'] and criteria['author'].lower() in book['autor'].lower()]
    if 'publish_date' in criteria:
        filtered_books = [book for book in filtered_books if book['publish_date'] == criteria['publish_date']]
    # Retorna a lista de livros filtrados
    return filtered_books