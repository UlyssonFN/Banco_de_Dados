#menu
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
        print("Bem vindo ao sistema")
    
    conexao.commit()
    conexao.close()
    
except Exception:
    print("Usuário ou Senha inválida")
    
    conexao.commit()
    conexao.close()





#Vou iniciar e vou terminar outro dia, porque a viagem hoje foi longa. 300km