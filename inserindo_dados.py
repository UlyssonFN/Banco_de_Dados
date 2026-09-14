#Tutorial 03 - Etapa de inserção de dados dentro do banco, precisamos dar vida a nossa tabela né!

#Importar a biblioteca
import sqlite3

#Abrir conexão com o banco de dados
conexao = sqlite3.connect("banco.bd")

#Criar o cursor
cursor = conexao.cursor()

#Executa o comando INSERT
#INSERT INTO significa inserir 1 novo registro na tabela.
cursor.execute("""
               INSERT INTO produtos (nome, preco, estoque)
               VALUES (?, ?, ?)
               """, ("Macbook", 1750, 1))

#Cria uma lista contendo vários produtos
#produtos = [ 
#    ("Mouse", 49.90, 20),
#    ("Monitor", 899.90, 8),
#    ("Teclado", 89.90, 15),
#    ("Headset", 149.90, 12)        
#            ]

#Insere todos os produtos da lista
#cursor.executemany("""
#    INSERT INTO produtos (nome, preco, estoque)
#    VALUES (?, ?, ?)
#    """, produtos)

#Salva o cadastro no banco.
conexao.commit()

#Fecha a conexão com o banco.
conexao.close()

#Enfeite de sempre
print("Produto cadastrado com sucesso!") 

#Um dica bem legal é que no lugar dos valores é possível colocar variáveis, ou seja, é possível criar inputs com interação de usuários para operarem sem mexer no código.


#PS: Todo dia postarei um novo código do projeto