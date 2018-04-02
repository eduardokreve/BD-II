# coding=utf-8
'''
Código para cuidar da manipulação de arquivos
'''

import os

#cria a pasta para guardar as tabelas
def createFolder():
    try: 
        os.mkdir('./Tables')
    except FileExistsError:
        #https://pt.stackoverflow.com/questions/72678/como-limpar-o-console-no-python
        os.system('cls' if os.name == 'nt' else 'clear')

#cria o arquivo binário com o nome da tabela
def createBin(name):    
    file = open('/Tables/name.txt', 'r')
    file.close()


