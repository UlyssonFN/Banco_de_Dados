#login

import sqlite3

conexao = sqlite3.connect("BDSYS.bd")

cursor = conexao.cursor()
try:
    user = input("Usuário: ")
    password = input("Senha: ")

    cursor.execute("""
                SELECT NOME FROM USUARIOS WHERE NOME=?""",(user,))

    (usuario,) = cursor.fetchone()

    cursor.execute("""
                SELECT SENHA FROM USUARIOS WHERE SENHA=?""",(password,))

    (senha,) = cursor.fetchone()

    if user == usuario and password == senha:
        from menu import opcoes
        opcoes
    
    conexao.commit()
    conexao.close()
    
except Exception:
    print("Usuário ou Senha inválida")
    
    conexao.commit()
    conexao.close() 