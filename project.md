Banco de dados utilizado PostgreSQL12
A criação das tabelas e inserção foram feitas pelo arquivo t1.py.
Utilizei a biblioteca psycopg2 para criar a conexão com o banco de dados, e utilizei a biblioteca
Pandas para a leitura do arquivo Contacts.xlsx

No banco foram utilizados 7 tabelas sendo:
  contato = onde ficam os nomes dos contatos do arquivo .xlsx
  telefone = onde ficam os telefones dos contatos do arquivo .xlsx
  email = onde ficam os e-mail(s) dos contatos do arquivo .xlsx
  localidade = onde foram inseridos algumas localidades ficticias e os ids dos contatos
  tipos_alerta = onde ficaram os três tipos de alerta Verde,Amarelo e Vermelho
  periodo = onde ficaram armazenados os dias da semana, horario e id dos contatos
  envio_alerta = onde ficam os ids todos vinculados
