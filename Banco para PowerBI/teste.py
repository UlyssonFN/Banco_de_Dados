#Criado somente para verificar as colunas das talebas por sou esquecido
import sqlite3

conexao = sqlite3.connect("BDSYS.bd")

cursor = conexao.cursor()

cursor.execute("""
               SELECT NAME 
                FROM PRAGMA_TABLE_INFO('USUARIOS');
               """)
mostrar = cursor.fetchall()
print(mostrar)

conexao.commit()

cursor.close()