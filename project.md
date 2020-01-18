
Para a codificação em python utilizei o pycharm
Para banco de dados foi utiliza o postgreSQL12

Bibliotecas utilizadas:
	pandas - para leitura do arquivo contacts.xlsx
	psycopg2 - para criar a conexão com o banco postgres

Preparação do ambiente
	1. Instalação pycharm https://www.jetbrains.com/pycharm/
	Foi utilizado a versão gratuita
	Baixar e instalar também o python https://www.python.org/downloads/
	
	2. Instalação do banco de dados postgreSQL12 https://www.enterprisedb.com/downloads/postgres-postgresql-downloads#windows
	Baixar a versão correspondente ao sistema operacional
	Para testar a versão contida aqui criar o banco com a senha '12345' ou alterar o password na linha 9 para a senha deseja.

	3. Inicializar o ícone pgAdimin4 para iniciar o banco de dados
	Fica junto a pasta do PostgreSQL 12 na barra iniciar(utilizando Windows)

	4. Quando o banco for inicializado ele abrirá uma pagina no broswer padrão do seu computador no meu caso utilizei o Edge.
	Clicar com botão direito em Databases
	Clicar em Create
	Clicar em Database
	Criar um novo banco com nome 'bd'

	5. Criar uma pasta no local desejado do seu computador com o arquivo t1.py na raiz e dentro desta pasta uma pasta chamada "arq" onde colocara	o arquivo que está em anexo
	chamado contacts.xlsx

	6. Abrir o pycharm, ir no icone 'File' depois 'Open' e indicar o caminho da pasta criada no item 5.

	7. Ainda no pycharm, ir no terminal e executar os seguintes comandos:
	pip install psycopg2
	pip install pandas
	pip install xlrd
	Fiz um por vez, porém se quiser pode ser feito desta forma também
	pip install psycopg2 pandas xlrd

	8. Rodar o arquivo t1.py no pycharm

	9. Na pagina do banco(no broswer) clicar com o botão direito em bd e clicar em refresh
	Isso atualizará o banco.

	10. Em Schemas > Tables você conseguirá ver que foram criada as tabelas e alimentados os dados do arquivo contacts.xlxs.

Explicando o código:
	Linhas 1 à 2 são as importações das bibliotecas.
	Linhas 4 à 6 função para inserir novo alerta passando o id_envioAlerta e id_contato que queira mandar o alerta
	Linhas 8 à 9 conexões com o banco
	Linhas 12 à 35 criando as tabelas no banco
	Linha 40 lendo o arquivo contacts.xlsx com a função read do pandas
	Linhas 42 à 53 inserindo os dados do arquivo contacts.xlsx no banco com auxilio da função iterrows do pandas
	Linha 44 faço um if para ver se não á duplicidade de dados no arquivo
	Linhas 56 à 61 faço dois while um para ficar rodando direto e outro para inserir 10 contatos na tabela envio_alerta
	Linha 63 commit no banco
	Linha 64 fechando a conexão




	
