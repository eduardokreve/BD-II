# coding=utf-8
'''
Código para cuidar da manipulação de arquivos
'''

import os
import string

#cria a pasta para guardar as paginas
def createFolder():
    try: 
        os.mkdir('./pages')
    except FileExistsError:
        #https://pt.stackoverflow.com/questions/72678/como-limpar-o-console-no-python
        os.system('cls' if os.name == 'nt' else 'clear')

#cria o arquivo com o nome da pagina
def createPage(namepage, page):    
    name = ''.join(namepage) + '.dat' #converte o nome para 'str' com extensão .bin

    os.chdir('pages/') #entra na pasta 

    try:
        file = open(name, 'r') #se o arquivo ja existe
        
    except:
        file = open(name, 'w') #senao abre um novo arquivo
        print("Criado um novo arquivo\n")
        
        #gravado no arquivo
        pageHeader = 0 #posição que ainda não foi usada no posDado
        posDado = 0 #em que posição da lista está o dado
        usado = 0 #se não está usado = 0, usado = 1

        item = [posDado, usado]
        page = ', '.join(map(str, page)) #converte para str
        item = str(item)

        file.write(str(pageHeader) + ' ')
        file.write('[' + item + page + ']')

    file.close()
    os.chdir('..') #sai da pasta 

#insere os valores no arquivo
def insertValue(namePage, valor):
    os.chdir('pages/') #entra na pasta
    
    try:
        file = open(namepage, 'r+') #leitura e escrita

        

        file.close()
        
    
    except:
        print("Arquivo não existe para gravar os dados!\n")

    os.chdir('..') #sai da pasta 