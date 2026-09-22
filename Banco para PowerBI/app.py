#menu
import sqlite3

conexao = sqlite3.connect("BDSYS.bd")

cursor = conexao.cursor()

cursor.execute("""
               INSERT INTO USUARIOS (NOME, NIVEL, SENHA, STATUS)
               VALUES (?, ?, ?, ?)           
               """,("admin","ADMIN",12345,"ATIVO"))

conexao.commit()

conexao.close()

#Nessa parte eu add um primeiro usuário no banco de dados, que é o admin, senão não será possível realizar o login com nenhum usuário. 