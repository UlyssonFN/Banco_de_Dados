# README — DB Browser for SQLite

Guia prático para utilização do **DB Browser for SQLite**, uma ferramenta gráfica para criar, visualizar e manipular bancos de dados SQLite.

---

## 1. O que é o DB Browser for SQLite?

O **DB Browser for SQLite** é uma interface gráfica que permite trabalhar com bancos de dados SQLite sem precisar executar todos os comandos pelo terminal.

Com ele é possível:

* Criar bancos de dados SQLite;
* Criar e alterar tabelas;
* Inserir registros;
* Consultar dados;
* Editar registros;
* Excluir registros;
* Executar comandos SQL;
* Importar e exportar dados;
* Visualizar a estrutura do banco;
* Criar índices;
* Analisar o banco de dados.

> **Importante:** o DB Browser é uma ferramenta para trabalhar com SQLite. O banco de dados continua sendo um banco **SQLite**, e os comandos SQL continuam sendo os mesmos.

---

## 2. Instalação

Baixe o DB Browser for SQLite no site oficial:

https://sqlitebrowser.org/

Após instalar, abra o programa.

As principais áreas da interface são:

* **Database Structure** — estrutura do banco de dados;
* **Browse Data** — visualização e edição dos registros;
* **Edit Pragmas** — configurações do SQLite;
* **Execute SQL** — execução de comandos SQL.

---

## 3. Criando um banco de dados

Para criar um novo banco:

**File → New Database**

Escolha o local onde deseja salvar o arquivo.

Exemplo:

```text
meu_projeto.db
```

O arquivo `.db` será o próprio banco de dados SQLite.

Também é comum encontrar bancos SQLite utilizando extensões como:

```text
.db
.sqlite
.sqlite3
```

A extensão utilizada não altera o fato de que o banco é SQLite.

---

## 4. Criando uma tabela

Depois de criar o banco, acesse:

**Database Structure → Create Table**

Como exemplo, vamos criar uma tabela chamada `produtos`.

| Campo   | Tipo    | Configuração                 |
| ------- | ------- | ---------------------------- |
| id      | INTEGER | Primary Key + Auto Increment |
| nome    | TEXT    | Not Null                     |
| preco   | REAL    |                              |
| estoque | INTEGER |                              |

A estrutura equivalente em SQL seria:

```sql
CREATE TABLE produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL,
    estoque INTEGER
);
```

Depois de criar a tabela, clique em:

**OK → Write Changes**

---

## 5. Write Changes

O botão **Write Changes** grava no arquivo do banco as alterações realizadas.

Isso se aplica a operações como:

* Criação de tabelas;
* Inserção de registros;
* Alteração de registros;
* Exclusão de registros;
* Alterações na estrutura do banco.

Após realizar alterações importantes, utilize:

**Write Changes**

para garantir que elas sejam persistidas no arquivo do banco.

---

## 6. Visualizando os dados

Acesse:

**Browse Data**

Depois selecione a tabela:

```text
produtos
```

Os registros existentes serão exibidos em formato de tabela.

Exemplo:

| id | nome    |  preco | estoque |
| -: | ------- | -----: | ------: |
|  1 | Teclado | 120.00 |      15 |
|  2 | Mouse   |  80.00 |      30 |
|  3 | Monitor | 850.00 |       8 |

---

## 7. Inserindo registros

É possível inserir registros utilizando a interface gráfica do **Browse Data**.

Também podemos utilizar SQL através da aba:

**Execute SQL**

Exemplo:

```sql
INSERT INTO produtos (nome, preco, estoque)
VALUES ('Teclado', 120.00, 15);
```

Depois clique em:

**Execute**

E, para salvar a alteração:

**Write Changes**

---

## 8. Consultando dados com SELECT

Na aba:

**Execute SQL**

execute:

```sql
SELECT * FROM produtos;
```

O `*` significa que todas as colunas serão retornadas.

Também podemos selecionar somente algumas colunas:

```sql
SELECT nome, preco
FROM produtos;
```

---

## 9. Filtrando registros com WHERE

Para encontrar produtos específicos, utilizamos `WHERE`.

Exemplo:

```sql
SELECT *
FROM produtos
WHERE estoque > 10;
```

Outro exemplo:

```sql
SELECT *
FROM produtos
WHERE preco > 100;
```

Também podemos combinar condições:

```sql
SELECT *
FROM produtos
WHERE preco > 100
AND estoque > 10;
```

---

## 10. Pesquisando textos com LIKE

O operador `LIKE` pode ser utilizado para pesquisar textos.

Exemplo:

```sql
SELECT *
FROM produtos
WHERE nome LIKE '%mouse%';
```

O caractere `%` representa qualquer sequência de caracteres.

A consulta:

```sql
LIKE '%mouse%'
```

pode encontrar valores como:

```text
Mouse
Mouse Gamer
Mouse sem fio
Mouse USB
```

---

## 11. Alterando registros

Para alterar registros utilizamos `UPDATE`.

Exemplo:

```sql
UPDATE produtos
SET preco = 150.00
WHERE id = 1;
```

Nesse caso, somente o produto cujo `id` é `1` será alterado.

Depois da alteração:

**Write Changes**

### Atenção

Sempre analise o `WHERE` antes de executar um `UPDATE`.

Por exemplo:

```sql
UPDATE produtos
SET preco = 150.00;
```

Esse comando altera o preço de **todos os registros da tabela**.

---

## 12. Excluindo registros

Para excluir um registro específico utilizamos `DELETE`.

Exemplo:

```sql
DELETE FROM produtos
WHERE id = 2;
```

Nesse caso, somente o registro com `id = 2` será excluído.

Depois:

**Write Changes**

### Atenção

O comando:

```sql
DELETE FROM produtos;
```

remove **todos os registros da tabela**.

A tabela continuará existindo, mas ficará vazia.

---

## 13. Diferença entre DELETE e DROP TABLE

### DELETE

```sql
DELETE FROM produtos;
```

Remove os registros da tabela.

A tabela continua existindo:

```text
produtos
├── id
├── nome
├── preco
└── estoque
```

Porém, seus registros serão removidos.

### DROP TABLE

```sql
DROP TABLE produtos;
```

Remove a tabela inteira.

Depois da execução, a tabela `produtos` não existirá mais no banco.

---

## 14. Ordenando resultados

Utilizamos `ORDER BY` para ordenar os resultados.

Preço do menor para o maior:

```sql
SELECT *
FROM produtos
ORDER BY preco ASC;
```

Preço do maior para o menor:

```sql
SELECT *
FROM produtos
ORDER BY preco DESC;
```

Onde:

* `ASC` = ordem crescente;
* `DESC` = ordem decrescente.

---

## 15. Limitando resultados

Para retornar somente cinco registros:

```sql
SELECT *
FROM produtos
LIMIT 5;
```

Podemos combinar `ORDER BY` com `LIMIT`.

Exemplo:

```sql
SELECT *
FROM produtos
ORDER BY preco DESC
LIMIT 5;
```

Nesse caso, serão retornados os cinco produtos com maior preço.

---

## 16. Funções de agregação

O SQLite possui diversas funções para realizar cálculos sobre os dados.

### Contar registros

```sql
SELECT COUNT(*)
FROM produtos;
```

### Maior preço

```sql
SELECT MAX(preco)
FROM produtos;
```

### Menor preço

```sql
SELECT MIN(preco)
FROM produtos;
```

### Preço médio

```sql
SELECT AVG(preco)
FROM produtos;
```

### Soma do estoque

```sql
SELECT SUM(estoque)
FROM produtos;
```

---

## 17. GROUP BY

O `GROUP BY` permite agrupar registros.

Exemplo:

```sql
SELECT categoria, COUNT(*)
FROM produtos
GROUP BY categoria;
```

Resultado:

| categoria   | COUNT(*) |
| ----------- | -------: |
| Informática |       15 |
| Escritório  |        8 |
| Eletrônicos |       12 |

O `GROUP BY` é muito utilizado em consultas analíticas e na construção de relatórios.

---

## 18. Criando relacionamento entre tabelas

Podemos criar uma tabela de categorias:

```sql
CREATE TABLE categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);
```

Depois podemos relacioná-la com a tabela `produtos`:

```sql
CREATE TABLE produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL,
    estoque INTEGER,
    categoria_id INTEGER,
    FOREIGN KEY (categoria_id)
        REFERENCES categorias(id)
);
```

Nesse exemplo, `categoria_id` será utilizado para relacionar um produto à sua categoria.

---

## 19. JOIN

O `JOIN` permite consultar informações relacionadas entre diferentes tabelas.

Exemplo:

```sql
SELECT
    produtos.nome,
    produtos.preco,
    categorias.nome AS categoria
FROM produtos
JOIN categorias
    ON produtos.categoria_id = categorias.id;
```

Exemplo de resultado:

| produto |  preco | categoria   |
| ------- | -----: | ----------- |
| Teclado | 120.00 | Informática |
| Mouse   |  80.00 | Informática |
| Cadeira | 900.00 | Escritório  |

---

## 20. Trabalhando pela aba Execute SQL

Uma boa forma de aprender SQLite é utilizar o DB Browser como interface visual e executar os comandos SQL diretamente pela aba **Execute SQL**.

Exemplo completo:

### Criar tabela

```sql
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT,
    idade INTEGER
);
```

### Inserir registro

```sql
INSERT INTO clientes (nome, email, idade)
VALUES ('João', 'joao@email.com', 30);
```

### Consultar

```sql
SELECT *
FROM clientes;
```

### Atualizar

```sql
UPDATE clientes
SET idade = 31
WHERE id = 1;
```

### Excluir

```sql
DELETE FROM clientes
WHERE id = 1;
```

---

## 21. O ponto e vírgula `;`

É recomendado finalizar os comandos SQL com `;`.

Exemplo:

```sql
SELECT * FROM produtos;
```

```sql
DELETE FROM produtos WHERE id = 5;
```

```sql
DROP TABLE produtos;
```

O `;` indica o final de uma instrução SQL.

Ele também é importante quando várias instruções são executadas no mesmo editor:

```sql
INSERT INTO produtos (nome, preco)
VALUES ('Teclado', 120.00);

INSERT INTO produtos (nome, preco)
VALUES ('Mouse', 80.00);

SELECT * FROM produtos;
```

---

## 22. Importando arquivos CSV

O DB Browser permite importar dados de arquivos CSV.

Normalmente:

**File → Import → Table from CSV File**

Selecione o arquivo `.csv`.

Durante a importação, verifique:

* Separador utilizado;
* Existência de cabeçalho;
* Nome da tabela;
* Tipos das colunas;
* Codificação do arquivo.

Depois confirme a importação e utilize:

**Write Changes**

---

## 23. Exportando dados

O DB Browser também permite exportar informações do banco.

Entre os formatos disponíveis estão:

* CSV;
* SQL;
* Estrutura do banco;
* Dados das tabelas.

Isso pode ser útil para utilizar os dados em ferramentas como:

* Excel;
* Power BI;
* Python;
* Pandas;
* Outros bancos de dados.

---

## 24. Backup do banco

Um banco SQLite normalmente pode ser armazenado em um único arquivo.

Exemplo:

```text
projeto.db
```

Um backup simples pode ser feito copiando esse arquivo:

```text
projeto.db
projeto_backup.db
```

Antes de executar operações destrutivas, é recomendado realizar um backup.

Exemplos de operações que exigem atenção:

```sql
DELETE
```

```sql
DROP TABLE
```

---

## 25. Comandos básicos para praticar

### Criar tabela

```sql
CREATE TABLE produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER DEFAULT 0
);
```

### Inserir produtos

```sql
INSERT INTO produtos (nome, preco, estoque)
VALUES ('Teclado', 120.00, 15);

INSERT INTO produtos (nome, preco, estoque)
VALUES ('Mouse', 80.00, 30);

INSERT INTO produtos (nome, preco, estoque)
VALUES ('Monitor', 850.00, 8);
```

### Consultar

```sql
SELECT *
FROM produtos;
```

### Filtrar

```sql
SELECT *
FROM produtos
WHERE preco > 100;
```

### Ordenar

```sql
SELECT *
FROM produtos
ORDER BY preco DESC;
```

### Atualizar

```sql
UPDATE produtos
SET estoque = 20
WHERE id = 1;
```

### Excluir

```sql
DELETE FROM produtos
WHERE id = 2;
```

---

## 26. Fluxo recomendado no DB Browser

Uma rotina básica para trabalhar com SQLite:

```text
Abrir DB Browser
       ↓
Criar ou abrir banco
       ↓
Criar tabela
       ↓
Inserir dados
       ↓
Consultar com SELECT
       ↓
Filtrar com WHERE
       ↓
Ordenar com ORDER BY
       ↓
Alterar com UPDATE
       ↓
Excluir com DELETE
       ↓
Salvar com Write Changes
```

---

## 27. Cuidados importantes

Sempre utilize `WHERE` quando a intenção for alterar ou excluir registros específicos.

Evite:

```sql
UPDATE produtos
SET preco = 100;
```

Prefira:

```sql
UPDATE produtos
SET preco = 100
WHERE id = 5;
```

Evite:

```sql
DELETE FROM produtos;
```

quando a intenção for excluir apenas um registro.

Prefira:

```sql
DELETE FROM produtos
WHERE id = 5;
```

Antes de executar `UPDATE`, `DELETE` ou `DROP TABLE`, verifique cuidadosamente o comando.

---

## 28. DB Browser x SQLite3

O **DB Browser for SQLite** e o **SQLite3** não são bancos de dados diferentes.

Ambos trabalham com o mesmo SQLite.

### DB Browser

```text
DB Browser
     ↓
SQLite
     ↓
arquivo .db
```

### Terminal

```text
SQLite3
   ↓
SQLite
   ↓
arquivo .db
```

Isso significa que um banco criado no DB Browser pode ser aberto posteriormente pelo terminal utilizando o SQLite3.

Também é possível utilizar o mesmo arquivo com Python.

---

## 29. SQLite + Python

O SQLite pode ser utilizado diretamente em aplicações Python.

Exemplo:

```python
import sqlite3

conexao = sqlite3.connect("produtos.db")

cursor = conexao.cursor()

cursor.execute("""
    SELECT *
    FROM produtos
""")

dados = cursor.fetchall()

for produto in dados:
    print(produto)

conexao.close()
```

Nesse cenário, o DB Browser pode ser utilizado para visualizar e administrar o banco enquanto o Python utiliza o SQLite como banco de dados da aplicação.

---

## 30. Principais comandos SQL

| Comando        | Função               |
| -------------- | -------------------- |
| `CREATE TABLE` | Criar tabela         |
| `INSERT INTO`  | Inserir dados        |
| `SELECT`       | Consultar dados      |
| `UPDATE`       | Alterar dados        |
| `DELETE`       | Excluir dados        |
| `DROP TABLE`   | Excluir tabela       |
| `WHERE`        | Filtrar registros    |
| `ORDER BY`     | Ordenar resultados   |
| `GROUP BY`     | Agrupar resultados   |
| `JOIN`         | Relacionar tabelas   |
| `COUNT()`      | Contar registros     |
| `SUM()`        | Somar valores        |
| `AVG()`        | Calcular média       |
| `MAX()`        | Retornar maior valor |
| `MIN()`        | Retornar menor valor |

---

## 31. Sequência recomendada de aprendizado

Para aprender SQLite utilizando o DB Browser, uma sequência prática é:

```text
CREATE TABLE
      ↓
INSERT INTO
      ↓
SELECT
      ↓
WHERE
      ↓
ORDER BY
      ↓
UPDATE
      ↓
DELETE
      ↓
GROUP BY
      ↓
JOIN
      ↓
Índices
      ↓
SQLite + Python
```

O DB Browser permite visualizar graficamente o resultado de cada operação, tornando mais fácil entender a relação entre os comandos SQL e os dados armazenados no banco.

---

## 32. Conclusão

O **DB Browser for SQLite** é uma ferramenta prática para estudar e administrar bancos SQLite por meio de uma interface gráfica.

Uma abordagem recomendada é utilizar o DB Browser para visualizar a estrutura e os dados do banco, enquanto os principais comandos são praticados pela aba **Execute SQL**.

Com o domínio dos comandos básicos, é possível evoluir para:

* Modelagem de bancos;
* Relacionamentos entre tabelas;
* Chaves primárias e estrangeiras;
* Índices;
* Consultas mais complexas;
* Agregações;
* Subconsultas;
* Views;
* Integração com Python;
* Aplicações utilizando SQLite como banco de dados.
