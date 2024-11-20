import getpass
import record_books_DB as rBook
import record_users_DB as rUser

# rBook.recordBook(
#     autor = input('Indique o nome do autor: '),
#     title_book = input('Indique o título da obra: '),
#     publish_date = input('Indique o ano da publicação: '),
#     genero_book = input('Indique o género da obra: ' + '\n' + 'Ex: Ação, Comédia, Drama, etc.')

# )

# rUser.recordUser(
#     nome = input('Indique o nome do Utilizador: '),
#     password = getpass.getpass('Indique a password: ', '*')
# )

books = rBook.get_all_books()
print(books)