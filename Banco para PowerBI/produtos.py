#cadastro de produtos
def cad_produtos_f():
    a = 1
    while a ==1:
        import sqlite3

        conexao = sqlite3.connect("BDSYS.bd")

        cursor = conexao.cursor()

        barcode = int(input("Digite o código de barras do produto: "))
        descricao = input("Digite a descrição do produto: ")
        valorC = float(input("Digite o valor de compra do produto: "))
        valorV = float(input("Digite o valor de venda do produto: "))
        qtd = int(input("Digite a quantidade do produto: "))


        cursor.execute("""
                    INSERT INTO PRODUTOS (COD_BARRA, DESCRICAO, VALOR_COMPRA, VALOR_VENDA, QUANTIDADE, STATUS )
                    VALUES (?, ?, ?, ?, ?, ?)""", (barcode, descricao, valorC, valorV, qtd, "ATIVO")) 

        conexao.commit()

        cursor.close()

        print("Cadastro realizado com sucesso")
     
        resp = input("Deseja realizar um novo cadastro? s/n: ")
        if resp == "s".lower():
            a = 1
        else:
            a = 0       
        
        

