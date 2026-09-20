# Banco criado para PowerBI

A ideia desse projeto é criar um banco de dados com algumas tabelas para ligarmos junto com o PowerBI, criando assim um dashboard interativo
Principal ideia criar um sistema backend com login, cadastro de usuários, produtos e vendas. 

# Estrutura do Sistema

login - cadastro de usuários - cadastro de produtos - venda de produtos
Criar regra de hierarquia de usuários (admin acesso a tudo, vendedor terá acesso somente a venda)

 - Criar banco de dados 
 - Criar tabelas
 - Criar menu.py
 - Criar usuario.py
 - Criar produtos.py
 - Criar vendas.py

# Estrutura Banco de dados

Tabelas {USUARIOS, PRODUTOS, VENDAS}

# Estrutura das Tabelas

{USUÁRIOS}

- ID - AUTOINCREMENT
- NOME
- NIVEL - VENDEDOR OU ADMIN
- SENHA
- STATUS - ATIVO OU INATIVO

{PRODUTOS}

- ID - AUTOINCREMENT
- COD_BARRA INTEGER UNIQUE NOT NULL
- DESCRICAO
- VALOR_COMPRA - FLOAT
- VALOR_VENDA - FLOAT
- QUANTIDADE - INTEGER
- STATUS - ATIVO OU INATIVO

{VENDAS}

- ID - AUTOINCREMENT
- COD_BARRA
- DESCCRICAO
- QUANTIDADE_VENDA - FLOAT
- VALOR_VENDA - FLOAT
- VALOR_TOTAL - FLOAT
- DATA
