#Tutorial 06 - Como realizar a exclusão de um registro

#Importa a biblioteca sqlite3
import sqlite3

#Cria a conexão com o banco de dados existente
conexao = sqlite3.connect('banco.bd')

#Criar o cursor de interação com o banco
cursor = conexao.cursor()

#Exclui o registro dentro da tabela
cursor.execute("""
    DELETE FROM produtos WHERE id = '3'                         
               """)

#Exclui a tabela
#DROP TABLE produtos;

#Deleta todos os registro da tabela
#DELETE FROM produtos;

#Modelo muito usado para dentro do parêntese ser usado uma váriavel
#cursor.execute("""
#    DELETE FROM produtos WHERE id = ?                         
#               """, ('2'))

#Salva a alteração
conexao.commit()

#Fecha a conexão
conexao.close()

#Informa que o produto foi excluido
print("Produto excluído com sucesso!!!!")
 