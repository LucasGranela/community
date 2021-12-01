CREATE TABLE PESSOA (
    CPF CHAR(11) PRIMARY KEY, --xxxxxxxxxxx
    EMAIL VARCHAR2(50) UNIQUE NOT NULL,
    NOME VARCHAR2(100) NOT NULL,
    TELEFONE CHAR(11) NOT NULL,-- xx9xxxxxxxx
    SENHA VARCHAR2(50) NOT NULL,
    NUMERO VARCHAR2(5),
    RUA VARCHAR2(100),
    BAIRRO VARCHAR2(100),
    CIDADE VARCHAR2(100),
    CEP CHAR(8) --XXXXXXXX
)

CREATE TABLE GUARDA (
    CPF CHAR(11) PRIMARY KEY, --xxxxxxxxxxx
    PERMISSAO VARCHAR2(50) UNIQUE NOT NULL

    CONSTRAINT FK_CPF FOREIGN KEY (CPF)
               REFERENCES PESSOA(CPF)
               ON DELETE CASCADE
)

CREATE TABLE SEGUIDOR(
    SEGUIDO CHAR(11),
    SEGUIDOR CHAR(11),

    CONSTRAINT PK_SEGUIDOR PRIMARY KEY (SEGUIDO, SEGUIDOR),
    CONSTRAINT FK_SEGUIDO FOREIGN KEY (SEGUIDO)
               REFERENCES PESSOA(CPF)
               ON DELETE CASCADE

    CONSTRAINT FK_SEGUIDOR FOREIGN KEY (SEGUIDOR)
               REFERENCES PESSOA(CPF)
               ON DELETE CASCADE
)

CREATE TABLE ORGANIZADOR (
    CPF CHAR(11) PRIMARY KEY, --xxxxxxxxxxx
    NOTA FLOAT,

    CONSTRAINT FK_CPF FOREIGN KEY (CPF)
               REFERENCES PESSOA(CPF)
               ON DELETE CASCADE
)

CREATE TABLE EVENTO(
    ID INT AUTOINCREMENT PRIMARY KEY,
    NOME VARCHAR2(50) NOT NULL,
    DATA_E_HORA TIMESTAMP NOT NULL,
    LONGITUDE CHAR(10) NOT NULL, --+OU-XX.XXXXXX
    LATITUDE CHAR(10) NOT NULL, --+OU-XX.XXXXXX
    TIPO INT NOT NULL, --0(FESTA), 1(SOCIAL), 2(SHOW), 3(ESPORTIVO), 4(DIVERSOS)
    NOTA FLOAT,
    ORGANIZADOR CHAR(11) NOT NULL, --xxxxxxxxxxx


    CONSTRAINT CK_TIPO_DE_EVENTO CHECK (TIPO = 0 OR TIPO = 1 OR TIPO = 2 TIPO = 3 OR TIPO = 4),
    CONSTRAINT UK2_EVENTO UNIQUE(NOME,DATA_E_HORA, LONGITUDE, LATITUDE),
    
    CONSTRAINT FK_ORGANIZADOR_EVENTO FOREIGN KEY (ORGANIZADOR)
               REFERENCES ORGANIZADOR(CPF)
               ON DELETE CASCADE
)

CREATE TABLE OCORRENCIA (
    ID INT AUTOINCREMENT PRIMARY KEY, 
    DATA_E_HORA TIMESTAMP NOT NULL,
    LONGITUDE CHAR(10) NOT NULL, --+OU-XX.XXXXXX
    LATITUDE CHAR(10) NOT NULL, --+OU-XX.XXXXXX
    TIPO INT NOT NULL, --0(CRIMINAL), 1(ESTRUTURAL)
    SUBTIPO INT NOT NULL, --0(FALTA DE LUZ), 1(VAZAMENTO DE AGUA), 2(ROUBO), 3(DIVERSOS)
    DESCRICAO VARCHAR2(100),
    CRIADOR CHAR(11), --xxxxxxxxxxx
    
    CONSTRAINT CK_TIPO_OCORRENCIA CHECK (TIPO = 0 OR TIPO = 1),
    CONSTRAINT CK_SUBTIPO_OCORRENCIA CHECK (SUBTIPO = 0 OR SUBTIPO = 1 OR SUBTIPO = 2 OR SUBTIPO = 3),

    CONSTRAINT UK2_OCORRENCIA UNIQUE(DATA_E_HORA, LONGITUDE, LATITUDE, TIPO, SUBTIPO),

    CONSTRAINT FK_CRIADOR_OCORRENCIA FOREIGN KEY (CRIADOR)
               REFERENCES PESSOA(CPF)
               ON DELETE SET NULL,
)

CREATE TABLE PARTICIPANTE(
    EVENTO INT,
    PESSOA CHAR(11),

    CONSTRAINT PK_PARTICIPANTE PRIMARY KEY (EVENTO, PESSOA),
    CONSTRAINT FK_EVENTO_PARTICIPANTE FOREIGN KEY (EVENTO)
               REFERENCES EVENTO(ID)
               ON DELETE CASCADE,

    CONSTRAINT FK_PESSOA_PARTICIPANTE FOREIGN KEY (PESSOA)
               REFERENCES PESSOA(CPF)
               ON DELETE CASCADE
)


CREATE TABLE CONTRATADO(
    GUARDA CHAR(11)
    EVENTO INT,
    STATUS INT NOT NULL,  --0(PENDENTE), 1(ACEITO), 2(RECUSADO)
    
    CONSTRAINT CK_STATUS_CONTRATADO CHECK (STATUS = 0 OR STATUS = 1 OR STATUS = 2),
    CONSTRAINT PK_CONTRATADO PRIMARY KEY (EVENTO, GUARDA),
    CONSTRAINT FK_EVENTO_CONTRATADO FOREIGN KEY (EVENTO)
               REFERENCES EVENTO(ID)
               ON DELETE CASCADE,

    CONSTRAINT FK_GUARDA_CONTRATADO FOREIGN KEY (GUARDA)
               REFERENCES GUARDA(CPF)
               ON DELETE CASCADE
)

CREATE TABLE PONTO_ESTRATEGICO (
    ID INT AUTOINCREMENT PRIMARY KEY,
    DATA_E_HORA TIMESTAMP NOT NULL,
    LONGITUDE CHAR(10) NOT NULL, --+OU-XX.XXXXXX
    LATITUDE CHAR(10) NOT NULL, --+OU-XX.XXXXXX
    TIPO INT NOT NULL, --0(BANCO), 1(RESTAURANTE), 2(BAR), 3(SORVETERIA), 4(LANCHONETE), 5(DIVERSOS)
    DESCRICAO VARCHAR2(200),
    CRIADOR CHAR(11), --xxxxxxxxxxx
    
    CONSTRAINT CK_TIPO_PONTO_ESTRATEGICO CHECK (TIPO = 0 OR TIPO = 1 OR TIPO = 2 OR TIPO = 3 OR TIPO = 4 OR TIPO = 5),
    
    CONSTRAINT UK2_PONTO_ESTRATEGICO UNIQUE(DATA_E_HORA, LONGITUDE, LATITUDE, TIPO),

    CONSTRAINT FK_CRIADOR_PONTO_ESTRATEGICO FOREIGN KEY (CRIADOR)
               REFERENCES PESSOA(CPF)
               ON DELETE CASCADE
)

CREATE TABLE POST (
    ID INT AUTOINCREMENT PRIMARY KEY,
    DATA_E_HORA TIMESTAMP NOT NULL,
    PESSOA CHAR(11) NOT NULL, --xxxxxxxxxxx
    MENSAGEM VARCHAR2(200) NOT NULL,

    CONSTRAINT UK2_POST UNIQUE(DATA_E_HORA, PESSOA),

    CONSTRAINT FK_PESSOA_POST FOREIGN KEY (PESSOA)
               REFERENCES PESSOA(CPF)
               ON DELETE CASCADE
)

CREATE TABLE POST_OCORRENCIA (
    POST INT PRIMARY KEY, --ID DO POST
    OCORRENCIA INT NOT NULL, --ID DA OCORRENCIA
    ESTADO INT NOT NULL DEFAULT 0, --0(NAO VERIFICADO), 1(EM ANDAMENTO), 2(VERIFICADO)
    
    CONSTRAINT CK_ESTADO_POST_OCORRENCIA CHECK (ESTADO = 0 OR ESTADO = 1 OR ESTADO = 2),
    
    CONSTRAINT FK_OCORRENCIA_POST_OCORRENCIA FOREIGN KEY (OCORRENCIA)
               REFERENCES OCORRENCIA(ID)
               ON DELETE CASCADE
)

CREATE TABLE POST_EVENTO (
    POST INT PRIMARY KEY, --ID DO POST
    EVENTO INT NOT NULL, --ID DO EVENTO
    
    CONSTRAINT FK_EVENTO_POST_EVENTO FOREIGN KEY (EVENTO)
               REFERENCES EVENTO(ID)
               ON DELETE CASCADE
)

CREATE TABLE POST_PONTO_ESTRATEGICO (
    POST INT PRIMARY KEY, --ID DO POST
    PONTO_ESTRATEGICO INT NOT NULL, --ID DO PONTO_ESTRATEGICO
    
    CONSTRAINT FK_PONTO_ESTRATEGICO_POST_PONTO_ESTRATEGICO FOREIGN KEY (PONTO_ESTRATEGICO)
               REFERENCES PONTO_ESTRATEGICO(ID)
               ON DELETE CASCADE
)

CREATE TABLE COMENTARIO (
    ID INT AUTOINCREMENT PRIMARY KEY,
    PESSOA CHAR(11) NOT NULL, --xxxxxxxxxxx
    POST INT NOT NULL, --ID DO POST
    DATA_E_HORA TIMESTAMP NOT NULL,
    MENSAGEM VARCHAR2(200) NOT NULL,

    CONSTRAINT UK2_COMENTARIO UNIQUE(PESSOA, POST, DATA_E_HORA),

    CONSTRAINT FK_PESSOA_COMENTARIO FOREIGN KEY (PESSOA)
               REFERENCES PESSOA(CPF)
               ON DELETE CASCADE,
    CONSTRAINT FK_POST_COMENTARIO FOREIGN KEY (POST)
               REFERENCES POST(ID)
               ON DELETE CASCADE
)



CREATE TABLE DELEGACIA (
    CNPJ CHAR(14) PRIMARY KEY, --XXXXXXXX0001XX
    DISTRITO VARCHAR2(7) NOT NULL, 
    NOME VARCHAR2(50) NOT NULL
)

CREATE TABLE ORGANIZACOES_DE_SERVICOS(
    CNPJ CHAR(14) PRIMARY KEY, --XXXXXXXX0001XX
    NOME VARCHAR2(50) NOT NULL
)

CREATE TABLE ESTRUTURAL (
    ID INT PRIMARY KEY, 
    ORGAO CHAR(18), --XXXXXXXX0001XX
    ESTADO INT NOT NULL DEFAULT 0, --0(NAO VERIFICADO), 1(EM ANDAMENTO), 2(VERIFICADO)

    CONSTRAINT CK_TIPO_ESTADO_ESTRUTURAL CHECK (ESTADO = 0 OR ESTADO = 1 OR ESTADO = 2),

    CONSTRAINT FK_ID_ESTRUTURAL FOREIGN KEY (ID)
               REFERENCES OCORRENCIA(ID)
               ON DELETE CASCADE,
    CONSTRAINT FK_ORGAO_ESTRUTURAL FOREIGN KEY (ORGAO)
               REFERENCES ORGANIZACOES_DE_SERVICOS(CNPJ)
               ON DELETE SET NULL
)

CREATE TABLE CRIMINAL (
    ID INT PRIMARY KEY, 
    DELEGACIA CHAR(14), --XXXXXXXX0001XX
    ESTADO INT NOT NULL DEFAULT 0, --0(NAO VERIFICADO), 1(EM ANDAMENTO), 2(VERIFICADO)
    IDEVENTO INT, --FK EVENTO

    CONSTRAINT CK_TIPO_ESTADO_CRIMINAL CHECK (ESTADO = 0 OR ESTADO = 1 OR ESTADO = 2),
    
    CONSTRAINT FK_ID_CRIMINAL FOREIGN KEY (ID)
               REFERENCES OCORRENCIA(ID)
               ON DELETE CASCADE,
    CONSTRAINT FK_DELEGACIA_CRIMINAL FOREIGN KEY (DELEGACIA)
               REFERENCES DELEGACIA(CNPJ)
               ON DELETE SET NULL,
    CONSTRAINT FK_ID_EVENTO FOREIGN KEY (IDEVENTO)
               REFERENCES EVENTO(ID)
               ON DELETE SET NULL
)



CREATE TABLE CIDADE_DE_OPERACAO (
    ORGAO CHAR(18), --XXXXXXXX0001XX
    CIDADE VARCHAR2(50),
    
    CONSTRAINT PK_CIDADE_DE_OPERACAO PRIMARY KEY (ORGAO, CIDADE),
    CONSTRAINT FK_ORGAO_CIDADE_DE_OPERACAO FOREIGN KEY (ORGAO)
               REFERENCES ORGANIZACOES_DE_SERVICOS(CNPJ)
               ON DELETE CASCADE
)