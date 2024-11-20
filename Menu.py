import os
import time
import getpass
import delete_users as dUser
import record_users_DB as rUser
import record_books_DB as rBook
import search_books as sBook

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_titulo(titulo):
    print("╔" + "═" * 50 + "╗")
    print(f"║{titulo:^50}║")
    print("╚" + "═" * 50 + "╝")

def exibir_menu():
    limpar_tela()
    exibir_titulo(" BIBLIOTECA MUNICIPAL DE ESTARREJA ")
    
    print("╔══════════════════════════════════════════════════╗")
    print("║ [1] Gerir Utilizadores                           ║")
    print("║     [1.1] Registar Novo Utilizador               ║")
    print("║     [1.2] Eliminar Utilizador                    ║")
    print("║ [2] Gerir Livros                                 ║")
    print("║     [2.1] Registar Novo Livro                    ║")
    print("║     [2.2] Remover Livro                          ║")
    print("║     [2.3] Atualizar Informações de um Livro      ║")
    print("║ [3] Empréstimos e Devoluções                     ║")
    print("║     [3.1] Registar Empréstimo                    ║")
    print("║     [3.2] Registar Devolução                     ║")
    print("║     [3.3] Organizar Fila de Espera               ║")
    print("║ [4] Consultar Histórico de Atividades            ║")
    print("║     [4.1] Histórico por Livro                    ║")
    print("║     [4.2] Histórico por Utilizador               ║")
    print("║ [5] Pesquisa e Consulta                          ║")
    print("║     [5.1] Pesquisa por Título                    ║")
    print("║     [5.2] Pesquisa por Autor                     ║")
    print("║     [5.3] Aplicar Filtros Específicos            ║")
    print("║ [6] Sistema de Recomendações                     ║")
    print("║ [7] Cópia de Segurança e Carregamento de Dados   ║")
    print("║ [8] Sair                                         ║")
    print("╚══════════════════════════════════════════════════╝")

def animacao_saida():
    limpar_tela()
    mensagem = "A sair do sistema... Até logo!"
    for char in mensagem:
        print(char, end="", flush=True)
        time.sleep(0.05)
    print("\n")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            print("\nGerir Utilizadores")
            sub_opcao = input("Escolha uma sub-opção (1.1 ou 1.2): ")

            if sub_opcao == '1.1':
                print("Registar Novo Utilizador")
                rUser.recordUser(
                                nome = input('\nIndique o nome do Utilizador: '),
                                password = getpass.getpass('\nO que digitar estará oculto, no final pressione ENTER.'+'\nIndique a password: ' , '*')
                                )
                
            elif sub_opcao == '1.2':
                print("Eliminar Utilizador")
                # dUser.get_user() #### Código ainda não está pronto - DV

            else:
                print("Sub-opção inválida!")
                
        elif opcao == '2':
            print("\nGerir Livros")
            sub_opcao = input("Escolha uma sub-opção (2.1, 2.2 ou 2.3): ")

            if sub_opcao == '2.1':
                print("Registar Novo Livro")
                autor = input('\nIndique o nome do autor: ')
                title_book = input('\nIndique o título da obra: ')
                publish_date = input('\nIndique o ano da publicação: ')
                genero_book = input('\nIndique o género da obra: ' + '\nEx: Ação, Comédia, Drama, etc.')

                rBook.recordBook(autor, title_book, publish_date, genero_book)

            elif sub_opcao == '2.2':
                print("Remover Livro")
                # Implementar função de eliminação de livro  
            elif sub_opcao == '2.3':
                print("Atualizar Informações de um Livro")
                # Implementar função de atualização de livro
            else:
                print("Sub-opção inválida!")
                
        elif opcao == '3':
            print("\nEmpréstimos e Devoluções")
            sub_opcao = input("Escolha uma sub-opção (3.1, 3.2 ou 3.3): ")
            if sub_opcao == '3.1':
                print("Registar Empréstimo")
                # Implementar função de registo de empréstimo
            elif sub_opcao == '3.2':
                print("Registar Devolução")
                # Implementar função de registo de devolução
            elif sub_opcao == '3.3':
                print("Organizar Fila de Espera")
                # Implementar função de fila de espera
            else:
                print("Sub-opção inválida!")
                
        elif opcao == '4':
            print("\nConsultar Histórico de Atividades")
            sub_opcao = input("Escolha uma sub-opção (4.1 ou 4.2): ")
            if sub_opcao == '4.1':
                print("Histórico por Livro")
                # Implementar função de histórico por livro
            elif sub_opcao == '4.2':
                print("Histórico por Utilizador")
                # Implementar função de histórico por utilizador
            else:
                print("Sub-opção inválida!")
                
        elif opcao == '5':
            print("\nPesquisa e Consulta")
            sub_opcao = input("Escolha uma sub-opção (5.1, 5.2 ou 5.3): ")
            if sub_opcao == '5.1':
                print("Pesquisa por Título")
                title = input('Indique o título da obra: ')
                books = sBook.search_by_title(title)
                print(books)
                input("Pressione Enter para continuar...")
            elif sub_opcao == '5.2':
                print("Pesquisa por Autor")
                author = input('Indique o nome do autor: ')
                books = sBook.search_by_author(author)
                print(books)
                input("Pressione Enter para continuar...")
            elif sub_opcao == '5.3':
                print("Aplicar Filtros Específicos")
                criteria = {
                    'title': input('Indique o título da obra: '),
                    'author': input('Indique o nome do autor: '),
                    'publish_date': input('Indique o ano da publicação: ')
                }
                remover_vazios = {}
                for key, value in criteria.items():
                    if value:
                        remover_vazios[key] = value

                criteria = remover_vazios
                books = sBook.filter_books(criteria)
                print(books)
                input("Pressione Enter para continuar...")
            else:
                print("Sub-opção inválida!")
                
        elif opcao == '6':
            print("\nSistema de Recomendações")
            # Implementar sistema de recomendações

        elif opcao == '7':
            print("\nCópia de Segurança e Carregamento de Dados")
            # Implementar função de cópia de segurança e carregamento de dados

        elif opcao == '8':
            animacao_saida()
            break

        else:
            print("\nOpção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
