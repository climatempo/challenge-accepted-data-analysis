import pandas as pd
import psycopg2

con = psycopg2.connect(host='localhost', database='bd', user='postgres', password='12345')
cur = con.cursor()

sql = 'create table contato (id_contato serial primary key, nome varchar(100))'
cur.execute(sql)
sql1 = 'create table telefone (id_telefone serial primary key, numero varchar(100))'
cur.execute(sql1)
sql2 = 'create table email (id_email serial primary key, email varchar(100))'
cur.execute(sql2)
sql3 = 'create table localidade (id_localidade serial primary key, id_contato serial, localidade varchar(100))'
cur.execute(sql3)
sql4 = 'create table tipos_alerta (id_tipoAlerta serial primary key, cor varchar(100))'
cur.execute(sql4)
sql5 = 'create table periodo (id_periodo serial primary key, id_contato serial, diaSemana varchar(100), horario varchar(100))'
cur.execute(sql5)
sql6 = 'create table envio_alerta (id_envioAlerta serial primary key, id_contato serial, id_localidade serial,id_tipoAlerta serial, id_periodo serial)'
cur.execute(sql6)



#Leitura arquivo com pandas
df = pd.read_excel('arq/Contacts.xlsx')

#Inserindo dados do arquivo Contacts.xlsx no Postgres
for index, linha in df.iterrows():
    cur.execute("INSERT INTO contato (id_contato, nome) VALUES (default, '%s')" %(linha['Nome']))

for index, linha1 in df.iterrows():
    cur.execute("INSERT INTO email (id_email, email) VALUES (default, '%s')" %(linha1['E-mail']))

for index, linha2 in df.iterrows():
    cur.execute("INSERT INTO telefone (id_telefone, numero) VALUES (default, '%s')" % linha2['Telefone'])

#Iserindo localidade
cur.execute("INSERT INTO localidade (id_localidade, id_contato, localidade) VALUES (default, 1,'região 1')")
cur.execute("INSERT INTO localidade (id_localidade, id_contato, localidade) VALUES (default, 2,'região 2')")
cur.execute("INSERT INTO localidade (id_localidade, id_contato, localidade) VALUES (default, 3,'região 3')")
cur.execute("INSERT INTO localidade (id_localidade, id_contato, localidade) VALUES (default, 4,'região 1')")

#Inserindo tipo de alerta
cur.execute("INSERT INTO tipos_alerta (id_tipoAlerta, cor ) VALUES ( 1,'verde')")
cur.execute("INSERT INTO tipos_alerta (id_tipoAlerta, cor ) VALUES ( 2,'amarelo')")
cur.execute("INSERT INTO tipos_alerta (id_tipoAlerta, cor ) VALUES ( 3,'vermelho')")

#Inserindo periodo
cur.execute("INSERT INTO periodo (id_periodo, id_contato, diaSemana, horario) VALUES (default, 1, 'Segunda-feira','1:00 às 13:00')")
cur.execute("INSERT INTO periodo (id_periodo, id_contato, diaSemana, horario) VALUES (default, 2, 'Terça-feira','8:00 às 19:00')")
cur.execute("INSERT INTO periodo (id_periodo, id_contato, diaSemana, horario) VALUES (default, 3, 'Quarta-feira','6:00 às 17:00')")
cur.execute("INSERT INTO periodo (id_periodo, id_contato, diaSemana, horario) VALUES (default, 4, 'Quinta-feira','8:00 às 20:00')")
cur.execute("INSERT INTO periodo (id_periodo, id_contato, diaSemana, horario) VALUES (default, 5, 'Domingo',' 19:00 às 5:00')")

#Inserindo alerta
cur.execute("INSERT INTO envio_alerta (id_envioAlerta, id_contato, id_localidade,id_tipoAlerta, id_periodo) VALUES (default,1,1,3,1)")
cur.execute("INSERT INTO envio_alerta (id_envioAlerta, id_contato, id_localidade,id_tipoAlerta, id_periodo) VALUES (default,2,2,1,2)")
cur.execute("INSERT INTO envio_alerta (id_envioAlerta, id_contato, id_localidade, id_tipoAlerta,id_periodo) VALUES (default,3,3,2,3)")

con.commit()
con.close()






