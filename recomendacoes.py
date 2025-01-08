import csv
import diretorios as dir

# Função para recomendar livros
def recomendar_livros_por_genero(utilizador):
    generos_requisitados = set()
    livros_recomendados = []

    # Carregar os empréstimos do utilizador e identificar os gêneros dos livros requisitados
    with open(dir.dirEmprestimos, 'r', newline='', encoding='latin-1') as emprestimos_file:
        lista_emprestimos = csv.reader(emprestimos_file)
        for emprestimo in lista_emprestimos:
            if len(emprestimo) >= 5 and emprestimo[4].strip() == utilizador.strip():
                titulo = emprestimo[0].strip()
                with open(dir.dirBooks, 'r', newline='', encoding='latin-1') as books_file:
                    lista_livros = csv.reader(books_file)
                    for livro in lista_livros:
                        if len(livro) == 4 and livro[1].strip() == titulo:
                            generos_requisitados.add(livro[3].strip())
                            break

    # Carregar todos os livros e recomendar aqueles que pertencem aos gêneros requisitados pelo utilizador
    with open(dir.dirBooks, 'r', newline='', encoding='latin-1') as books_file:
        lista_livros = csv.reader(books_file)
        for livro in lista_livros:
            if len(livro) == 4 and livro[3].strip() in generos_requisitados:
                livros_recomendados.append(livro)

    return livros_recomendados
