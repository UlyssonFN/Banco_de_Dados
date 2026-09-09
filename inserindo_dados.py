#Etapa de inserção de dados dentro do banco
#Importar a biblioteca
import sqlite3

#Abrir conexão com o banco de dados
conexao = sqlite3.connect("banco.bd")

#Criar o cursor
cursor = conexao.cursor()

#Executa o comando INSERT
#INSERT INTO significa inserir um novo registro na tabela.
cursor.execute("""
               INSERT INTO produtos (nome, preco, estoque)
               VALUES (?, ?, ?)
               """, ("He4rt", 0.01, 1000))

#Salva o cadastro no banco.
conexao.commit()

#fecha a conexão com o banco.
conexao.close()

#enfeite de sempre
print("Produto cadastrado com sucesso!") 

#Um dica bem legal é que no lugar dos valores é possível colocar variáveis, ou seja, é possível criar inputs com interação de usuários para operarem sem mexer no código.
