-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2020-01-16 11:36:04.245

-- tables
-- Table: Alerta_Meio
CREATE TABLE Alerta_Meio (
    id_alerta_meio serial  NOT NULL,
    sms boolean  NULL,
    email boolean  NULL,
    call boolean  NULL,
    push boolean  NULL,
    whatsapp boolean  NULL,
    CONSTRAINT Alerta_Meio_pk PRIMARY KEY (id_alerta_meio)
);

-- Table: CNT_Contato
CREATE TABLE CNT_Contato (
    id_contato serial  NOT NULL,
    nome varchar(50)  NULL,
    Alerta_Meio_id_alerta_meio int  NOT NULL,
    CONSTRAINT nome_de_contato UNIQUE (nome) NOT DEFERRABLE  INITIALLY IMMEDIATE,
    CONSTRAINT Contato_pk PRIMARY KEY (id_contato)
);

-- Table: Envio_Alerta
CREATE TABLE Envio_Alerta (
    id_envio_alerta serial  NOT NULL,
    Tipos_Alertas_id_tipo_alerta int  NOT NULL,
    CNT_Contato_id_contato int  NOT NULL,
    LOC_Localidade_id_localidade int  NOT NULL,
    PRO_Periodo_id_periodo int  NOT NULL,
    MAIL_Email_email varchar(50)  NOT NULL,
    TEL_Telefone_DDI varchar(2)  NOT NULL,    
    TEL_Telefone_DDD varchar(2)  NOT NULL,
    TEL_Telefone_Tel_numero varchar(9)  NOT NULL,
    CONSTRAINT Envio_Alerta_pk PRIMARY KEY (id_envio_alerta)
);

-- Table: LOC_Localidade
CREATE TABLE LOC_Localidade (
    id_localidade serial  NOT NULL,
    nome_regiao varchar(50)  NULL,
    CNT_Contato_id_contato int  NOT NULL,
    
    CONSTRAINT Localidade_pk PRIMARY KEY (id_localidade)
);

-- Table: MAIL_Email
CREATE TABLE MAIL_Email (
    email varchar(50)  NOT NULL,
    CNT_Contato_id_contato int  NOT NULL,
    CONSTRAINT Email_pk PRIMARY KEY (email)
);

-- Table: PRO_Periodo
CREATE TABLE PRO_Periodo (
    id_periodo serial  NOT NULL,
    hora_inicial time  NULL,
    hora_final time  NULL,
    dom boolean  NULL,
    seg boolean  NULL,
    ter boolean  NULL,
    qua boolean  NULL,
    qui boolean  NULL,
    sex boolean  NULL,
    sab boolean  NULL,
    CNT_Contato_id_contato int  NOT NULL,
    
    CONSTRAINT Periodo_pk PRIMARY KEY (id_periodo)
);

-- Table: TEL_Telefone
CREATE TABLE TEL_Telefone (
    CNT_Contato_id_contato int  NOT NULL,
    DDI varchar(2)  NOT NULL,
    DDD varchar(2)  NOT NULL,
    Tel_numero varchar(9)  NOT NULL,
    CONSTRAINT Telefone_pk PRIMARY KEY (Tel_numero,DDD,DDI)
);

-- Table: Tipos_Alertas
CREATE TABLE Tipos_Alertas (
    id_tipo_alerta serial  NOT NULL,
    alerta_verde boolean  NULL,
    alerta_amarelo boolean  NULL,
    alerta_vermelho boolean  NULL,
    CNT_Contato_id_contato int  NOT NULL,
    
    CONSTRAINT Tipos_Alertas_pk PRIMARY KEY (id_tipo_alerta)
);

-- foreign keys
-- Reference: CNT_Contato_Alerta_Meio (table: CNT_Contato)
ALTER TABLE CNT_Contato ADD CONSTRAINT CNT_Contato_Alerta_Meio
    FOREIGN KEY (Alerta_Meio_id_alerta_meio)
    REFERENCES Alerta_Meio (id_alerta_meio)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Envio_Alerta_CNT_Contato (table: Envio_Alerta)
ALTER TABLE Envio_Alerta ADD CONSTRAINT Envio_Alerta_CNT_Contato
    FOREIGN KEY (CNT_Contato_id_contato)
    REFERENCES CNT_Contato (id_contato)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Envio_Alerta_LOC_Localidade (table: Envio_Alerta)
ALTER TABLE Envio_Alerta ADD CONSTRAINT Envio_Alerta_LOC_Localidade
    FOREIGN KEY (LOC_Localidade_id_localidade)
    REFERENCES LOC_Localidade (id_localidade)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Envio_Alerta_MAIL_Email (table: Envio_Alerta)
ALTER TABLE Envio_Alerta ADD CONSTRAINT Envio_Alerta_MAIL_Email
    FOREIGN KEY (MAIL_Email_email)
    REFERENCES MAIL_Email (email)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Envio_Alerta_PRO_Periodo (table: Envio_Alerta)
ALTER TABLE Envio_Alerta ADD CONSTRAINT Envio_Alerta_PRO_Periodo
    FOREIGN KEY (PRO_Periodo_id_periodo)
    REFERENCES PRO_Periodo (id_periodo)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Envio_Alerta_TEL_Telefone (table: Envio_Alerta)
ALTER TABLE Envio_Alerta ADD CONSTRAINT Envio_Alerta_TEL_Telefone
    FOREIGN KEY (TEL_Telefone_Tel_numero, TEL_Telefone_DDD, TEL_Telefone_DDI)
    REFERENCES TEL_Telefone (Tel_numero, DDD, DDI)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Envio_Alerta_Tipos_Alertas (table: Envio_Alerta)
ALTER TABLE Envio_Alerta ADD CONSTRAINT Envio_Alerta_Tipos_Alertas
    FOREIGN KEY (Tipos_Alertas_id_tipo_alerta)
    REFERENCES Tipos_Alertas (id_tipo_alerta)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: LOC_Localidade_CNT_Contato (table: LOC_Localidade)
ALTER TABLE LOC_Localidade ADD CONSTRAINT LOC_Localidade_CNT_Contato
    FOREIGN KEY (CNT_Contato_id_contato)
    REFERENCES CNT_Contato (id_contato)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: MAIL_Email_CNT_Contato (table: MAIL_Email)
ALTER TABLE MAIL_Email ADD CONSTRAINT MAIL_Email_CNT_Contato
    FOREIGN KEY (CNT_Contato_id_contato)
    REFERENCES CNT_Contato (id_contato)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: PRO_Periodo_CNT_Contato (table: PRO_Periodo)
ALTER TABLE PRO_Periodo ADD CONSTRAINT PRO_Periodo_CNT_Contato
    FOREIGN KEY (CNT_Contato_id_contato)
    REFERENCES CNT_Contato (id_contato)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Tel_Telefone_CNT_Contato (table: TEL_Telefone)
ALTER TABLE TEL_Telefone ADD CONSTRAINT Tel_Telefone_CNT_Contato
    FOREIGN KEY (CNT_Contato_id_contato)
    REFERENCES CNT_Contato (id_contato)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Tipos_Alertas_CNT_Contato (table: Tipos_Alertas)
ALTER TABLE Tipos_Alertas ADD CONSTRAINT Tipos_Alertas_CNT_Contato
    FOREIGN KEY (CNT_Contato_id_contato)
    REFERENCES CNT_Contato (id_contato)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

