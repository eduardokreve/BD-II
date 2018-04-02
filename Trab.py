# coding=utf-8
import string

#função que cria a tabela 
def criaTable(tab):  
    table = list(map(str, tab.split()))#converte o argumento para uma lista
    del table[0:2]#exclui create e table da lista

    nameTable = table[0:1]#pega o nome da tabela

    #faz a limpeza do comando ficando somente o atributo e tipo
    del table[0:1]
    del table[0:1]
    del table[len(table) -1 : len(table)] 
    
    while(1): #tira todas s ','
        try:
            del table[table.index(',')]
        except ValueError:
            break
   
    print(table)
    
#função que insere valores na tabela
def inseTable(valor):
    print("funcao que insere os valores")


def main():
    print("Insira espaço entre ',' e parenteses")
    print("Ex.: create table dados ( id int , letra char )\n\n")

    while(1): 
        
        comand = input("Comando SQL:")#a entrada é str
        
        #verifica os comandos SQL digitados corretamente 
        if(comand.find("create ") != -1 and comand.find("table ") != -1 and 
            comand.find("(") != -1 and comand.find(")")): 
            
            criaTable(comand)

        elif(comand.find("insert ") != -1 and comand.find("into ") != -1 and
             comand.find("(") != -1 and comand.find(")")):
            
            inseTable(comand)

        else:
            print("Comando incorreto")
            break

if __name__ == "__main__":
    main()
