import csv
import diretorios as dir

# Função consultar histórico por livro
def consultar_historico_por_livro(titulo_livro):
    historico = []
    with open(dir.dirHistorico, 'r') as historico_file:
        lista_historico = csv.reader(historico_file)
        for entrada in lista_historico:
            if len(entrada) >= 3 and entrada[0].strip().lower() == titulo_livro.strip().lower():
                historico.append(entrada)
    return historico

# Função consultar histórico por utilizador
def consultar_historico_por_utilizador(nome_utilizador):
    historico = []
    with open(dir.dirHistorico, 'r') as historico_file:
        lista_historico = csv.reader(historico_file)
        for entrada in lista_historico:
            if len(entrada) >= 3 and entrada[4].strip().lower() == nome_utilizador.strip().lower():
                historico.append(entrada)
    return historico