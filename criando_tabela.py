import sqlite3

conexao = sqlite3.connect("banco.bd")
#criar a variável chamada cursor, o cursor é utilizado para enviar o comandos SQL para o banco
cursor = conexao.cursor()

#Executa um comando SQL, no nosso caso abaixo está sendo criado nossa first table. (Duolingo desenrolado viu) 
cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                preco REAL NOT NULL,
                estoque INTERGER DEFAULT 0
                   
               )
               """)
#Confirma a alteração no banco, o commit grava definitivamente a operação
conexao.commit()
#Fecha nosso banco de dados
conexao.close()

#mostra uma msginha do coração
print("Tabela criada com sucesso ")