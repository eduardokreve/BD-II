# coding=utf-8
'''
Código para cuidar da manipulação de arquivos
'''

import os
import string

#cria a pasta para guardar as tabelas
def createFolder():
    try: 
        os.mkdir('./Tables')
    except FileExistsError:
        #https://pt.stackoverflow.com/questions/72678/como-limpar-o-console-no-python
        os.system('cls' if os.name == 'nt' else 'clear')

#cria o arquivo binário com o nome da tabela
def createBin(nameTable):    
    name = ''.join(nameTable) + '.bin'#converte o nome para 'str' com extensão .bin

    os.chdir('Tables/')#entra na pasta 

    try:
        file = open(name, 'r')#se o arquivo ja existe ele abre para ler
        print("Arquivo ja existe\n")
    except:
        file = open(name, 'w')#senao abre um novo
        print("Criado um novo arquivo\n")

    file.close()
    os.chdir('..')#sai da pasta
    

    



