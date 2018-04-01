# coding=utf-8

#função que cria a tabela 
def criaTable(tab):
    print("deu certo ")




def main():

    comand = input("Comando SQL: ")

    if(comand.find("create") != -1): #se for igual a -1 não foi achado
        criaTable(comand)
    else:
        print("erro")


if __name__ == "__main__":
    main()
