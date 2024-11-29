import record_books_DB as rb

# rb.recordBook(
#     autor = input('Indique o nome do autor: '),
#     title_book = input('Indique o título da obra: '),
#     publish_date = input('Indique o ano da publicação: ')
# )

books = rb.get_all_books()
print(books)