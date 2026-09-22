#menu
import sqlite3

conexao = sqlite3.connect("BDSYS.bd")

user = input("Usuário: ")
password = input("Senha: ")


cursor = conexao.cursor()

conexao.commit()

conexao.close()





#Vou iniciar e vou terminar outro dia, porque a viagem hoje foi longa. 300km