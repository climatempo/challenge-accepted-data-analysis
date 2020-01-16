import postgresql #install: pip install postgresql
from openpyxl import load_workbook #install: pip install openpyxl

caminho = 'C:/Users/Willian/Downloads/contacts.xlsx'
arquivo_excel = load_workbook(caminho)
#abrindo arquivo
db = postgresql.open("pq://postgres:admin@localhost:5432/bd")
#conexão com bd (user:password@host:port/database)
array = []
aux = []
contador = 0

def tipos_alertas(array, contador):
    for select_contato in db.prepare("select id_contato from public.cnt_contato"):
        array.append(select_contato)
    for i in arquivo_excel['alertas']:
        verde = False
        amarelo = False
        vermelho = False
        insert_tipo_alerta = db.prepare(
            "INSERT INTO tipos_alertas (alerta_verde, alerta_amarelo,alerta_vermelho, cnt_contato_id_contato) VALUES ($1,$2,$3,$4)")
        if(i[8].value == 'sim'):
            verde = True
        if(i[9].value == 'sim'):
            amarelo = True
        if(i[10].value == 'sim'):
            vermelho = True
        insert_tipo_alerta(verde, amarelo, vermelho, array[contador][0])
        contador += 1     

def alerta_meio():
    for i in arquivo_excel['alertas']:
        sms = False
        email = False
        call = False
        push = False
        whatsapp = False
        insert_alerta_meio = db.prepare("insert into public.alerta_meio (sms, email, call, push, whatsapp) values ($1, $2, $3, $4, $5)")
        if i[3].value != 'sms' or i[4].value != 'email' or i[5].value != 'call' or i[6].value != 'push' or i[7].value != 'whatsapp':
            if i[3].value == 'sim':
                sms = True
            if i[4].value == 'sim':
                email = True
            if i[5].value == 'sim':
                call = True
            if i[6].value == 'sim':
                push = True
            if i[7].value == 'sim':
                whatsapp = True
            insert_alerta_meio(sms,email, call, push, whatsapp)

def contato(array, contador):
    for var in db.prepare("select id_alerta_meio from public.alerta_meio"):
        array.append(var)
    for i in arquivo_excel['alertas']:
        insert_contato = db.prepare("insert into public.cnt_contato (nome, alerta_meio_id_alerta_meio) values ($1, $2)")
        if i[0].value != 'nome':
            nome_contato = i[0].value        
            insert_contato(nome_contato,array[contador][0])
            contador += 1

def telefone(array, contador):
    for select_contato in db.prepare("select id_contato from public.cnt_contato"):
        array.append(select_contato)
    for i in arquivo_excel['alertas']:
        a = i[2].value
        a = a.replace('telefone', '0 0 0').split(' ')
        insert_telefone = db.prepare("insert into public.tel_telefone (tel_numero, cnt_contato_id_contato, ddd, ddi) values ($1, $2, $3, $4)")
        if a[0] != '0':
            insert_telefone (a[2], array[contador][0], a[1], a[0])
            contador += 1

def email(array,contador):
    for select_contato in db.prepare("select id_contato from public.cnt_contato"):
        array.append(select_contato)
    for i in arquivo_excel['alertas']:
        insert_email = db.prepare('insert into public.mail_email (email, cnt_contato_id_contato) values ($1, $2)')
        if i[1].value != 'email':
            insert_email(i[1].value, array[contador][0])
            contador += 1
        
def localidade(array, contador, aux):
    for select_contato in db.prepare("select id_contato from public.cnt_contato"):
        aux.append(select_contato)
    for i in arquivo_excel['alertas']:
        insert_localidade = db.prepare('insert into public.loc_localidade ( nome_regiao, cnt_contato_id_contato ) values ($1, $2)')
        if i[20].value != 'regiao' and i[20].value not in array:
            array.append(i[20].value)
            insert_localidade(i[20].value, aux[contador][0])  
            contador += 1

def periodo(array, contador):
    for select_contato in db.prepare("select id_contato from public.cnt_contato"):
        array.append(select_contato)
    for i in arquivo_excel['alertas']:
        dom = False
        seg = False
        ter = False
        qua = False
        qui = False
        sex = False
        sab = False
        if i[11].value != 'hora_inicial' or i[12].value != 'hora_final' or i[13].value != 'dom' or i[14].value != "seg" or i[15].value != 'ter' or i[16].value != 'qua' or i[17].value != 'qui' or i[18].value != 'sex' or i[19].value != 'sab':
            periodo = db.prepare("insert into pro_periodo (dom, seg, ter, qua, qui, sex, sab, cnt_contato_id_contato, hora_inicial, hora_final) values ($1, $2, $3, $4, $5, $6, $7, $8, TO_TIMESTAMP("+"'"+i[11].value+"'"+",'HH24:MI'), TO_TIMESTAMP("+"'"+i[12].value+"'"+",'HH24:MI'))")
            if i[13].value == 'sim':
                dom = True 
            if i[14].value == 'sim':
                seg = True
            if i[15].value == 'sim':
                ter = True
            if i[16].value == 'sim':
                qua = True
            if i[17].value == 'sim':
                qui = True
            if i[18].value == 'sim':
                sex = True
            if i[19].value == 'sim':
                sab = True
            periodo(dom,seg,ter,qua,qui,sex,sab,array[contador][0])
            contador += 1

def envio_alerta():
    for i in db.prepare("select id_contato from public.cnt_contato"):
        insert_envio_alerta = db.prepare("insert into envio_alerta (tipos_alertas_id_tipo_alerta, cnt_contato_id_contato, loc_localidade_id_localidade, pro_periodo_id_periodo, mail_email_email, tel_telefone_tel_numero, tel_telefone_ddd, tel_telefone_ddi) values ($1, $2, $3, $4, $5, $6, $7, $8)")
        
        for var in db.prepare("select id_tipo_alerta from public.tipos_alertas where cnt_contato_id_contato = '"+str(i[0])+"'"):
            a = var
        for var in db.prepare("select id_localidade from public.loc_localidade where cnt_contato_id_contato = '"+str(i[0])+"'"):
            b = var
        for var in db.prepare("select id_periodo from public.pro_periodo where cnt_contato_id_contato = '"+str(i[0])+"'"):
            c = var
        for var in db.prepare("select email from public.mail_email where cnt_contato_id_contato = '"+str(i[0])+"'"):
            d = var
        for var in db.prepare("select tel_numero, ddd, ddi from public.tel_telefone where cnt_contato_id_contato = '"+str(i[0])+"'"):
            e = var
        
        insert_envio_alerta(a[0],i[0],b[0],c[0],d[0],e[0],e[1],e[2])            
            
##start
alerta_meio()
contato(array, contador)
tipos_alertas(array, contador)
telefone(array, contador)
email(array,contador)
localidade(array, contador, aux)
periodo(array, contador)
envio_alerta()
#end
db.close()