import record_books_DB as rb
import diretorios as dir
import csv

# Filtra a lista de livros pelo título fornecido, seja em maiúsculas ou minúsculas
def search_by_title(title):
    books = rb.get_all_books()  # Adicione esta linha para depuração  # Adicione esta linha para depuração
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
    if 'title' in criteria and criteria['title']:
        filtered_books = [book for book in filtered_books if criteria['title'].lower() in book['title_book'].lower()]
    if 'author' in criteria and criteria['author']:
        filtered_books = [book for book in filtered_books if criteria['author'].lower() in book['autor'].lower()]
    if 'publish_date' in criteria and criteria['publish_date']:
        filtered_books = [book for book in filtered_books if book['publish_date'] == criteria['publish_date']]
    if 'genero_book' in criteria and criteria['genero_book']:
        filtered_books = [book for book in filtered_books if criteria['genero_book'].lower() in book['genero_book'].lower()]

    return filtered_books

# Função para procurar um livro pelo título        
def procurar_info_livro(titulo):
    titulo_do_livro = titulo
    
    with open(dir.dirBooks, 'r') as file:
        lista_livros = csv.reader(file)
        for livro in lista_livros:
                if titulo_do_livro == livro[1].strip():  
                    informacao_livro = livro
                    return informacao_livro
