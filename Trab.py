# coding=utf-8

#função que cria a tabela 
def criaTable(tab):
    print("deu certo ")




def main():

    while(1): 
        comand = input("Comando SQL: ")

        #verifica os comandos SQL digitados corretamente 
        if(comand.find("create") != -1 and comand.find("table") != -1): 
            criaTable(comand)

        elif(comand.find("insert") != -1 and comand.find("into") != -1):
            
        
        else:
            print("Comando incorreto")
            break



if __name__ == "__main__":
    main()
