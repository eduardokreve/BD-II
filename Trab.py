# coding=utf-8
import string

#função que cria a tabela 
def criaTable(tab):
    test = tab.split("create table")
    print(test)  
      




    

#função que insere valores na tabela
def inseTable(valor):
    print("funcao que insere os valores")


def main():

    while(1): 
        comand = input("Comando SQL:")

        #verifica os comandos SQL digitados corretamente 
        if(comand.find("create") != -1 and comand.find("table") != -1): 
            criaTable(comand)

        elif(comand.find("insert") != -1 and comand.find("into") != -1):
            inseTable(comand)

        else:
            print("Comando incorreto")
            break

if __name__ == "__main__":
    main()
