import csv
import diretorios as dirs
import getpass
from datetime import datetime

#### código ainda em construção - DV

def getUserToRemove():
    utilizador = input('Indique o Utilizador que pretende remover: ')
    
    infoUserToRemove = []

    with open(dirs.dirUsers, 'r') as file:
        listaUsers = file.readline()

        for nome in listaUsers:
            if nome == utilizador:
                infoUserToRemove.append[utilizador]
 
    # if dirs.passAdmin == getpass.getpass('Introduza a password de administrador: ', '*'):
    #     for utilizador in 
 
    return infoUserToRemove
    
    
i = getUserToRemove()
print(i)
