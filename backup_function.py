from datetime import datetime
import csv
import diretorios as dir

# def backup():
    
#     # Backup do repositório dos Livros
#     with open(dir.dirBooks, 'r') as book:
#         infoBooks = book.read()
#     with open(dir.dirBooksBackup, "a") as guardarBackupBooks:
#         guardarBackupBooks.write(infoBooks)
    
#     # Backup do repositório dos Users
#     with open(dir.dirUsers, 'r') as users:
#         infoUsers = users.read()
#     with open(dir.dirUsersBackup, "a") as guardarBackupUsers:
#         guardarBackupUsers.write(infoUsers)

#     # Backup do repositório de Fila de espera
#     with open(dir.dirFilaEspera, 'r') as filaEspera:
#         infoFilaEspera = filaEspera.read()
#     with open(dir.dirFilaEsperaBackup, "a") as guardarBackupFilaEspera:
#         guardarBackupFilaEspera.write(infoFilaEspera)

#     # Backup do repositório de Empréstimos
#     with open(dir.dirEmprestimos, 'r') as emprestimos:
#         infoEmprestimos = emprestimos.read()
#     with open(dir.dirEmprestimosBackup, "a") as guardarBackupEmprestimos:
#         guardarBackupEmprestimos.write(infoEmprestimos)

#     print("Backup dos repositórios realizado com sucesso.")


