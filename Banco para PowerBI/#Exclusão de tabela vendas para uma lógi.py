#Exclusão de tabela vendas para uma lógica mais estruturada

import sqlite3

conexao = sqlite3.connect("BDSYS.bd")

cursor = conexao.cursor()

cursor.execute("""
             DROP TABLE VENDAS;  
               """)


conexao.commit()

cursor.close()