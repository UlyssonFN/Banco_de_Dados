#Importa a biblioteca
import sqlite3
#Realiza a conexão com o banco de dados.
conexao = sqlite3.connect("banco.bd")
#Cria o comando cursor
cursor = conexao.cursor()
#Executa o Select para buscar todos os produtos
cursor.execute("SELECT * FROM produtos")
#Recupera todos os registros encontrados (Comando fetchall usado para retornar vários produtos.
produtos = cursor.fetchall()
#Percorre cada produto encontrado
for produto in produtos:
    #Mostra o resultado do que foi encontrado
    print(produto)

#Trás o registro com base no filtro, o comando fetchone usado para trazer 1 produto)
cursor.execute("""SELECT nome, preco FROM produtos WHERE nome=?""",('Macbook',))
#também pode ser feito via método de escrita SQL
#cursor.execute("SELECT nome, preco FROM produtos WHERE nome='Macbook'")

#Percorre cada produto encontrado
produtos = cursor.fetchone()
for nome in produtos:
    #Mostra o resultado do que foi encontrado
    print(nome)
    
#Fecha a conexão com o banco de dados
conexao.close()
