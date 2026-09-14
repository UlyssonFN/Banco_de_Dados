#Tutorial 05  - Como atualizar um dado já inputado dentro do banco de dados

#Importar Biblioteca
import sqlite3

#Conectar com o banco de dados
conexao = sqlite3.connect("banco.bd")

#Criação de cursor interativo com o banco
cursor = conexao.cursor()

#Atualizar estoque, é importante saber qual registro você quer atualizar, iremos trabalhar com o 1° registro, antes o valor de 1000 e agora vai se tornar -3
cursor.execute("""
    UPDATE produtos SET id = 2 WHERE id = '8'           
               """)

#Neste exemplo, podemos chamar o estoque atual e acrescentar + 100.
#cursor.execute("""
#    UPDATE produtos SET estoque = estoque + 100 WHERE id = '1'           
#               """)

#Segue também outro formato de alteração, esse é bem interessante, pois podemos declarar um input com váriável antes de tudo e coloca-lo para o usuário alterar, sem precisar codificar no back.
#cursor.execute("""
#    UPDATE produtos SET estoque = -3 WHERE id = ?           
#               """, ('1'))

#Salva a alteração
conexao.commit()

#Fecha o banco de dados
conexao.close()

