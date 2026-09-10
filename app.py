#Tutorial 01 - Nesse pequeno código iremos aprender a como criar um banco de dados em SQLite.

#Importa a biblioteca sqlite3, ela permite que o Python trabalhe com bancos de dados SQLite - é um banco mais simples nativo, e muito funcional.
import sqlite3

#Cria uma conexão com o banco de dados, se o arquivo "banco.bd" não existir, o SQLIte ira cria-lo de forma automatica. 
conexao = sqlite3.connect("banco.bd")

#Exibe a msg para mostrar que deu tudo certo rsrs!
print("Banco conectado com sucesso!")

#Fecha a conexão com o banco de dados, vai observar que muito dos nossos códigos vão sempre fechar, o SQLite em particular não tem um bom desempenho em muitos acessos simutâneos! 
conexao.close()

#PS: Todo dia postarei um novo código do projeto