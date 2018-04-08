# coding=utf-8
import string
import os
import fileFunction

#função que cria a pagina 
def createpage(pag):  
    page = list(map(str, pag.split())) #converte o parametro para uma lista
    del page[0:2] #exclui create e page da lista

    namePag = page[0:1] #pega o nome da pagina
    
    #faz a limpeza do comando ficando somente o atributo e tipo
    del page[0:2]
    del page[len(page) -1 : len(page)] 
    
    while(1): #tira todas as ',' da lista
        try:
            del page[page.index(',')]
        except ValueError:
            break

    #A manipulação dos arquivos é feita no fileFunction.py
    fileFunction.createFolder() 
    fileFunction.createPage(namePag, page)

    
#função que insere valores nas paginas
def insertpage(valor):
    valor = list(map(str, valor.split())) #converte o parametro para uma lista
    del valor[0:2] #exclui INSERT e INTO da lista
    
    namePag = valor[0:1] #pega o nome da pagina

    del valor[0:3] #exclui o nome e VALUES
    del valor[len(valor) -1 : len(valor)] 

    while(1): #tira todas as ',' da lista
        try:
            del valor[valor.index(',')]
        except ValueError:
            break
    
    fileFunction.insertValue(namePag, valor)


def main():
    print("Insira espaço entre ',' e parenteses\n")
    print("Ex.: create page dados ( int id , char letra )")
    print("     insert into dados value ( 10 , a )\n\n")

    while(1): 
        
        comand = input("Comando SQL:") #a entrada é str
    #    os.system('cls' if os.name == 'nt' else 'clear') #limpar a tela
        
        #verifica os comandos SQL digitados corretamente 
        if(comand.find("create ") != -1 and comand.find("page ") != -1 and 
            comand.find("(") != -1 and comand.find(")") != -1): 
            
            createpage(comand)
            
        elif(comand.find("insert ") != -1 and comand.find("into ") != -1 and
             comand.find("(") != -1 and comand.find(")") != -1):
            
            insertpage(comand)

        else:
            print("Comando incorreto")
            break
            

if __name__ == "__main__":
    main()
