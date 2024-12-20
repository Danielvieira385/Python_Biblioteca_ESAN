import pandas as pd

def recomendar_livros(utilizador):
    # Carregar dados
    emprestimos = pd.read_csv('repositorios/emprestimos_DB.csv', header=None, names=['titulo', 'utilizador', 'data_emprestimo', 'data_devolucao', 'data_retorno'])
    livros = pd.read_csv('repositorios/books_DB.csv', header=None, names=['autor', 'titulo', 'ano', 'genero'])

    # Filtrar empréstimos do utilizador
    emprestimos_utilizador = emprestimos[emprestimos['utilizador'] == utilizador]

    # Obter géneros dos livros emprestados
    generos_emprestados = livros[livros['titulo'].isin(emprestimos_utilizador['titulo'])]['genero'].unique()

    # Recomendar livros do mesmo género
    recomendacoes = livros[livros['genero'].isin(generos_emprestados) & ~livros['titulo'].isin(emprestimos_utilizador['titulo'])]

    return recomendacoes[['titulo', 'autor', 'genero']].to_dict(orient='records')