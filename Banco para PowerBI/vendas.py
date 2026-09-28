#vendas
import sqlite3
import datetime as dt

data = dt.datetime.today()

conexao = sqlite3.connect("BDSYS.bd")

cursor = conexao.cursor()

barcode = int(input("Bipe o código de barra: "))

#Descrição
cursor.execute("""
               SELECT DESCRICAO FROM PRODUTOS WHERE COD_BARRA = (?);
               """,(barcode,))
product = cursor.fetchone()
#Valor Unidade
cursor.execute("""
               SELECT VALOR_VENDA FROM PRODUTOS WHERE COD_BARRA = (?);
               """,(barcode,))
valor_unidade = cursor.fetchone()
#Valor Total
cursor.execute("""
               SELECT COD FROM PRODUTOS WHERE COD_BARRA = (?);
               """,(barcode,))

qtd = int(input("Digite a quantidade"))



print(product)

cursor.execute("""
               SELECT COD_BARRA, DESCRICAO, VALOR_COMPRA, VALOR_VENDA, QUANTIDADE FROM PRODUTOS WHERE COD_BARRA = (?);
               """,(barcode,))


add = input("Adicionar produto? Press Enter")

if add == "":
    cursor.execute("""
                   INSERT INTO VENDAS ('COD_BARRA', 'DESCRICAO', 'QUANTIDADE_VENDA', 'VALOR_VENDA', 'VALOR_TOTAL', 'DATA')""",(barcode))
    print("Produto adcionado")
else:
    print("Nova Compra? s/n")
    resp = input(" ")
    if resp == "s" or resp == "S":
        a = 1
    else:
        a = 0
        print("Finalização do programa")
        from menu import opcoes
        opcoes()



conexao.commit()

cursor.close()