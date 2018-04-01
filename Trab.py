# coding=utf-8
import string

#função que cria a tabela 
def criaTable(tab):  
    nameTable = list(map(str, tab.split())) #converte o argumento para uma lista

    del nameTable[0:2]#exclui create e table da lista
    
    print(nameTable)
      


#função que insere valores na tabela
def inseTable(valor):
    print("funcao que insere os valores")


def main():

    while(1): 
        comand = input("Comando SQL:")#a entrada é str
        
        #verifica os comandos SQL digitados corretamente 
        if(comand.find("create ") != -1 and comand.find("table ") != -1): 
            criaTable(comand)

        elif(comand.find("insert") != -1 and comand.find("into") != -1):
            inseTable(comand)

        else:
            print("Comando incorreto")
            break

if __name__ == "__main__":
    main()
