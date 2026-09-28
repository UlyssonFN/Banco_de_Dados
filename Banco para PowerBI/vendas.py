#vendas
def vendas_f():
    import sqlite3
    import datetime as dt
    from menu import opcoes_f

    a = 1

    while a ==1:
        data = dt.datetime.today()

        conexao = sqlite3.connect("BDSYS.bd")

        cursor = conexao.cursor()

        barcode = int(input("Bipe o código de barra: "))

        #Descrição
        cursor.execute("""
                    SELECT DESCRICAO FROM PRODUTOS WHERE COD_BARRA = (?);
                    """,(barcode,))
        (product,) = cursor.fetchone()
        #Valor Unidade
        cursor.execute("""
                    SELECT VALOR_VENDA FROM PRODUTOS WHERE COD_BARRA = (?);
                    """,(barcode,))
        (valor_unidade,) = cursor.fetchone()
        qtd = int(input("Digite a quantidade: "))
        valor_total = float(valor_unidade * qtd)

        print("O seu produto é ",product," quantidade em unidades compradas é: ",qtd," o valor unidade é: ",valor_unidade," o valor total da compra fica: ",round(valor_total,2)," a data da compra é: ", data)

        add = input("Adicionar produto? Press Enter:")

        if not add:
            cursor.execute("""
                    INSERT INTO VENDAS (COD_BARRA, DESCRICAO, QUANTIDADE_VENDA, VALOR_VENDA, VALOR_TOTAL, DATA) VALUES (?,?,?,?,?,?);"""
                    ,(barcode, product, qtd, valor_unidade, valor_total, data))
            print("Produto adcionado")
            conexao.commit()
            cursor.close()    
            
            resp = input("Nova Compra? s/n: ")

            if resp == "s" or resp == "S":
                a = 1
            else:
                a = 0
                print("Finalização do programa")
                opcoes_f()

               

        