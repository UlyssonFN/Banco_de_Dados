#usuarios
def user():
    import sqlite3

    conexao = sqlite3.connect("BDSYS.bd")

    cursor = conexao.cursor()

    nome = input("Insira o nome de cadastro: ")
    nivelr = input("Insira 1 para ADMIN ou 2 para OPERADOR: ")
    if nivelr == 1:
        nivel = "ADMIN"
    else:
        nivel = "OPERADOR"

    senha = input("Insira a senha de cadastro: ")


    cursor.execute("""
        INSERT INTO USUARIOS (NOME, NIVEL, SENHA, STATUS)
        VALUES (?, ?, ?, ?)""", (nome, nivel, senha, "ATIVO"))

    conexao.commit()

    cursor.close()

    print("Cadastro realizado com sucesso! ")
    
call = user()