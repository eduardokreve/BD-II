# coding=utf-8
import string
import os
import fileFunction

#função que cria a tabela 
def createTable(tab):  
    table = list(map(str, tab.split()))#converte o argumento para uma lista
    del table[0:2]#exclui create e table da lista

    nameTable = table[0:1]#pega o nome da tabela
    
    #faz a limpeza do comando ficando somente o atributo e tipo
    del table[0:2]
    del table[len(table) -1 : len(table)] 
    
    while(1): #tira todas as ','
        try:
            del table[table.index(',')]
        except ValueError:
            break

    #A manipulação dos arquivos é feita no fileFunction.py
    fileFunction.createFolder() 
    fileFunction.createBin(nameTable)


    
#função que insere valores na tabela
def insertTable(valor):
    print("funcao que insere os valores")


def main():
    print("Insira espaço entre ',' e parenteses")
    print("Ex.: create table dados ( id int , letra char )\n\n")

    while(1): 
        
        comand = input("Comando SQL:")#a entrada é str
        os.system('cls' if os.name == 'nt' else 'clear')#limpar a tela
        
        #verifica os comandos SQL digitados corretamente 
        if(comand.find("create ") != -1 and comand.find("table ") != -1 and 
            comand.find("(") != -1 and comand.find(")") != -1): 
            
            createTable(comand)
            
        elif(comand.find("insert ") != -1 and comand.find("into ") != -1 and
             comand.find("(") != -1 and comand.find(")") != -1):
            
            insertTable(comand)

        else:
            print("Comando incorreto")
            break
            

if __name__ == "__main__":
    main()
