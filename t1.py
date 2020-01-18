import pandas as pd
import psycopg2

#FUNCAO PARA INSERIR ALERTA PELO ID_CONTATO
def inserirAlerta(a,b):
    return cur.execute("INSERT INTO envio_alerta (id_envioAlerta, id_contato) VALUES (%d,%d)" %(a,b))

#CRIANDO AS CONEXOES PARA O BANCO POSTGRES
con = psycopg2.connect(host='localhost', database='bd', user='postgres', password='12345')
cur = con.cursor()

#CRIANDO A TABELA CONTATO
sql = 'create table contato (id_contato serial primary key, nome varchar(100))'
cur.execute(sql)
#CRIANDO A TABELA TELEFONE
sql1 = 'create table telefone (id_telefone serial primary key,id_contato serial, numero varchar(100))'
cur.execute(sql1)
#CRIANDO A TABELA EMAIL
sql2 = 'create table email (id_email serial primary key,id_contato serial, email varchar(100))'
cur.execute(sql2)
#CRIANDO A TABELA LOCALIDADE
sql3 = 'create table localidade (id_localidade serial primary key, id_contato serial, localidade varchar(100))'
cur.execute(sql3)
#CRIANDO A TABELA TIPOS_ALERTA
sql4 = 'create table tipos_alerta (id_tipoAlerta serial primary key,id_contato serial, verde varchar(100), amarelo varchar(100), vermelho varchar(100))'
cur.execute(sql4)
#CRIANDO A TABELA PERIODO
sql5 = 'create table periodo (id_periodo serial primary key, id_contato serial, horarioInicial varchar(100), horarioFinal varchar(100), dom varchar(100),seg varchar(100),ter varchar(100),qua varchar(100), qui varchar(100), sex varchar(100), sab varchar(100))'
cur.execute(sql5)
#CRIANDO A TABELA TIPO_ENVIO
sql6 = 'create table tipo_envio(id_tipoEnvio serial primary key, id_contato serial, sms varchar(100), email varchar(100), call varchar(100), push varchar(100), whatsapp varchar(100))'
cur.execute(sql6)
#CRIANDO A TABELA ENVIO_ALERTA
sql7 = 'create table envio_alerta (id_envioAlerta serial primary key, id_contato serial)'
cur.execute(sql7)



#Leitura arquivo com pandas
df = pd.read_excel('arq/contacts.xlsx')

#Inserindo dados do arquivo Contacts.xlsx no Postgres
for index, linha in df.iterrows():
    if((cur.execute("SELECT nome FROM contato where id_contato = %d" %index)  == linha['nome'])):
        break
    else:
        cur.execute("INSERT INTO contato (id_contato, nome) VALUES (default, '%s')" %(linha['nome']))
        cur.execute("INSERT INTO email (id_email,id_contato, email) VALUES (default, default, '%s')" % (linha['emailContato']))
        cur.execute("INSERT INTO telefone (id_telefone, id_contato, numero) VALUES (default, default, '%s')" % linha['telefone'])
        cur.execute("INSERT INTO localidade (id_localidade, id_contato, localidade) VALUES (default, default ,'%s')" % linha['regiao'])
        cur.execute("INSERT INTO tipos_alerta (id_tipoAlerta, id_contato, verde, amarelo, vermelho ) VALUES ( default, default, '%s', '%s', '%s')" % (linha['alerta_verde'], linha['alerta_amarelo'], linha['alerta_vermelho']))
        cur.execute("INSERT INTO periodo (id_periodo, id_contato, horarioInicial, horarioFinal, dom,seg,ter, qua, qui, sex, sab) VALUES (default, default,'%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(linha['hora_inicial'],linha['hora_final'],linha['dom'],linha['seg'],linha['ter'],linha['qua'],linha['qui'],linha['sex'],linha['sab']))
        cur.execute("INSERT INTO tipo_envio (id_tipoEnvio, id_contato, sms, email, call, push, whatsapp) VALUES (default,default,'%s','%s','%s','%s','%s')" % (linha['sms'], linha['email'], linha['call'], linha['push'], linha['whatsapp']))

#Inserindo alerta
while True:
    x = 1
    while x <= 10:
        idContato = int(input("Inserir o id do contato desejado: "))
        inserirAlerta(x,idContato)
        x = x + 1
    break

con.commit()
con.close()






