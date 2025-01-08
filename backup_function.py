import datetime 
import diretorios as dir

# Função para realizar o backup dos repositórios
def realizarBackupRepositorios():
    # Registo da data e hora do backup
    with open(dir.dirInfoBackupDisponivel, 'w') as backup_info:
        backup_info.write(f"\nCópia de segurança realizado em: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M')}") 
        repositorios = ["Livros", "Users", "Fila de espera", "Empréstimos", "Histórico de ações"]
        repositorios_str = ", ".join(repositorios)
        backup_info.write(f"\nCópia de segurança contem informação dos seguintes repositórios:\n{repositorios_str}.") 
    
    # Backup do repositório dos Livros
    with open(dir.dirBooks, 'r') as book:
        infoBooks = book.read()
    with open(dir.dirBooksBackup, "w") as guardarBackupBooks:
        guardarBackupBooks.write(infoBooks)
    
    # Backup do repositório dos Users
    with open(dir.dirUsers, 'r') as users:
        infoUsers = users.read()
    with open(dir.dirUsersBackup, "w") as guardarBackupUsers:
        guardarBackupUsers.write(infoUsers)

    # Backup do repositório de Fila de espera
    with open(dir.dirFilaEspera, 'r') as filaEspera:
        infoFilaEspera = filaEspera.read()
    with open(dir.dirFilaEsperaBackup, "w") as guardarBackupFilaEspera:
        guardarBackupFilaEspera.write(infoFilaEspera)

    # Backup do repositório de Empréstimos
    with open(dir.dirEmprestimos, 'r') as emprestimos:
        infoEmprestimos = emprestimos.read()
    with open(dir.dirEmprestimosBackup, "w") as guardarBackupEmprestimos:
        guardarBackupEmprestimos.write(infoEmprestimos)
        
    # Backup do repositorio de Histórico de Empréstimos
    with open(dir.dirHistorico, 'r') as historico:
        infoHistorico = historico.read()
    with open(dir.dirHistoricoBackup, "w") as guardarBackupHistorico:
        guardarBackupHistorico.write(infoHistorico)   
    
    print("Cópia de Segurança dos repositórios realizado com sucesso:\nLivros, Users, Fila de espera, Empréstimos e Historico de ações.")

# Função para repor os repositórios a partir do backup
def reporBackupRepositorios():
    # Reposição do repositório dos Livros
    with open(dir.dirBooksBackup, 'r') as bookBackup:
        infoBooksBackup = bookBackup.read()
    with open(dir.dirBooks, "w") as reporBackupBooks:
        reporBackupBooks.write(infoBooksBackup)
    
    # Reposição do repositório dos Users
    with open(dir.dirUsersBackup, 'r') as usersBackup:
        infoUsersBackup = usersBackup.read()
    with open(dir.dirUsers, "w") as reporBackupUsers:
        reporBackupUsers.write(infoUsersBackup)

    # Reposição do repositório da Fila de espera
    with open(dir.dirFilaEsperaBackup, 'r') as filaEsperaBackup:
        infoFilaEsperaBackup = filaEsperaBackup.read()
    with open(dir.dirFilaEspera, "w") as reporBackupFilaEspera:
        reporBackupFilaEspera.write(infoFilaEsperaBackup)

    # Reposição do repositório de Empréstimos
    with open(dir.dirEmprestimosBackup, 'r') as emprestimosBackup:
        infoEmprestimosBackup = emprestimosBackup.read()
    with open(dir.dirEmprestimos, "w") as reporBackupEmprestimos:
        reporBackupEmprestimos.write(infoEmprestimosBackup)
    
    # Reposição do repositorio de Histórico de Empréstimos
    with open(dir.dirHistoricoBackup, 'r') as historicoBackup:
        infoHistoricoBackup = historicoBackup.read()
    with open(dir.dirHistorico, "w") as reporBackupHistorico:
        reporBackupHistorico.write(infoHistoricoBackup)

    print("Reposição dos repositórios realizada com sucesso:\nLivros, Users, Fila de espera, Empréstimos e Historico de ações.")