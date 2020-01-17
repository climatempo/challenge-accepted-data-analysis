<p align="center">
  <a href="http://www.climatempo.com.br">
      <img src="http://i.imgur.com/Q9lCAMF.png" alt="Climatempo" width="300px"/>
  </a>
</p>

___

# Leitor de arquivos xlsx para json

Pega arquivo xlsx e transforma para json, podendo ser criada funções para trabalhar com qualquer banco de dados ou mandar para um servidor kafka.

## Como utilizar?

1. Clonar este repositório para poder utilizar.

```
$ git clone git clone https://github.com/pliniopereira/challenge-accepted-data-analysis.git
$ cd challenge-accepted-data-analysis/
```

2.Você pode utilizar docker para subir e conseguir visualizar algo parecido com messageria.

```
$ docker build -t analisador_xlsx .
$ docker run --rm analisador_xlsx
```
O arquivo processado .json está no docker nescessitando fazer docker cp para pegar arquivos dentro do docker.

3. Caso deseje rodar localmente basta ter o pip instalar e rodar o seguinte comando.
```
$ pip install -r requirements.txt  .
$ python3 run.py
```
O arquivo .json estara na pasta /processed.


### Você deverá:

1. Fazer um fork desse projeto no seu github; :heavy_check_mark:

2. Desenvolva! Você terá **7 dias** a partir da data do envio do desafio. :heavy_check_mark:

3. Criar o banco de dados utilizando o SGBD que quiser, mas achamos o uso do Postgres mais interessante :D

Resolvi desenvolver um script que pega arquivos .xlsx no momento e transforma em .json. Para fazer um arquivo sql utilizaria a biblioteca **psycopg2**. 

Achei interessante utilizar isso como a vaga "Inclusão, exclusão e alteração de grande massa de dados via arquivos (Excel, CSV, JSON ou similar)" achei que no futuro possa se usar o conceito de  ***messageria*** e  ***kafka*** pra ficar processando arquivos(Excel, CSV, JSON ou similar) e mandando para o kafka e depois fazer outro app em docker que pegasse do kafka e mandaria pro Postgres. 

4. Desenvolver um script em **Python** ou **Nodejs** para realizar a inserção dos dados do arquivo **contacts.xlsx** no banco de dados; :heavy_check_mark:

5. Nos enviar um pull request contendo o arquivo **.sql** com a criação das tabelas, o **script** criado para realizar a inserção no banco e um arquivo em markdown chamado **PROJECT.md** contando um pouco sobre o seu desenvolvimento para o teste e como podemos testá-lo :D :heavy_check_mark:

6. Envie um e-mail para **curriculo@climatempo.com.br** com seu **currículo** com o assunto: **Vaga de Estágio - Análise de Dados** e o **link do seu pull request**. :heavy_check_mark:


___
