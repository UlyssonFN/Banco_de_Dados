#Tutorial 02 - Iremos aprender a como criar uma tabela dentro do banco de dados que acabamos de criar no tutorial 01.

#Importando a biblioteca do SQLite
import sqlite3

#Estabelece a conexão com o banco de dados
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

#Explicando sobre a criação da tabela
#Criar a tabela chamada produtos
#CREATE TABLE IF NOT EXISTS produtos

#Cria a coluna id, INTERGER significa número inteiro, PRIMARY KEY identifica cada registro de forma única, AUTOINCREMENT o número preenche de forma automática em ordem.
#id INTEGER PRIMARY KEY AUTOINCREMENT,

#Cria a coluna preco, REAL é utilizado para números com casas decimais, NOT NULL quer dizer que o valor da coluna não pode ser nulo/vazio.
#preco REAL NOT NULL,

#Cria a coluna estoque, INTEGER já sabe o que é né? Número inteiro, DEFAULT 0 significa que, senão informarmos estoque o valor será automaticamente 0
#estoque INTEGER DEFAULT 0

#PS: Todo dia postarei um novo código do projeto