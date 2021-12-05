-- 0.1) Inserir pessoa
    
    INSERT INTO PESSOA 
    VALUES (<CPF>, <EMAIL>, <NOME>, <TELEFONE>, <SENHA>, <NUMERO>, <RUA>, <BAIRRO>, <CIDADE>, <CEP>)
    
-- 0.2) Inserir Organizador
    EXECUTE INSERIR_ORGANIZADOR(<ICPF>, <IEMAIL>, <INOME>, <ITELEFONE>, <ISENHA>, <INUMERO>, <IRUA>, <IBAIRRO>, <ICIDADE>, <ICEP>);

-- 0.3) Inserir Guarda
    EXECUTE INSERIR_ORGANIZADOR(<ICPF>, <IEMAIL>, <INOME>, <ITELEFONE>, <ISENHA>, <INUMERO>, <IRUA>, <IBAIRRO>, <ICIDADE>, <ICEP>, <IPERMISSAO>);

-- 0.4) Inserir Post
    EXECUTE INSERIR_POST(<data_hora (TIMESTAMP)>, <CPF>, <MENSAGEM>);

-- 1) evento ordenado por data

    SELECT E.NOME, E.DATA_E_HORA, E.LONGITUDE, E.LATITUDE
    FROM EVENTO E
    ORDER BY DATA_E_HORA;

-- 2) listar os X post mais novos geral

    SELECT PO.ID AS NUM_POST, PO.DATA_E_HORA, P.NOME AS CRIADOR, PO.MENSAGEM
    FROM POST PO JOIN PESSOA P
    ON PO.PESSOA = P.CPF 
    ORDER BY PO.DATA_E_HORA
    LIMIT <QUANTIDADE>

-- 3) listar os X post mais novos sobre eventos

    SELECT PO.ID AS NUM_POST, PO.DATA_E_HORA, PO.MENSAGEM, P.NOME AS CRIADOR, E.NOME AS NOME_EVENTO, E.DATA_E_HORA AS DATA_E_HORA_EVENTO, E.LATITUDE, E.LONTITUDE
    FROM POST_EVENTO PE, EVENTO E, PESSOA P, POST PO
    WHERE PE.EVENTO = E.ID AND PO.PESSOA = P.ID
    ORDER BY PO.DATA_E_HORA
    LIMIT <QUANTIDADE>

-- 4) listar os X post mais novos sobre Ocorrencias 

-- 5) listar os X post mais novos sobre Ponto estratégico

-- 6) Postar sobre eventos

-- 7) Listar eventos pela data_hora

    SELECT E.NOME, E.LATITUDE, E.LONGTITUDE , E.TIPO, E.ORGANIZADOR
    FROM EVENTO E 
    WHERE E.DATA_E_HORA = <DATA_E_HORA>

-- 8) Listar eventos pelo local

    SELECT E.NOME, E.DATA_E_HORA, E.TIPO, E.ORGANIZADOR
    FROM EVENTO E 
    WHERE E.LATITUDE = <LATITUDE> AND E.LONGITUDE = <LONGITUDE>


-- 9) Listar eventos pelo tipo

    SELECT E.NOME, E.DATA_E_HORA, E.LATITUDE, E.LONGTITUDE, E.ORGANIZADOR
    FROM EVENTO E 
    WHERE E.TIPO = <TIPO>

-- 10) Listar eventos que voce criou pela data

    SELECT E.NOME, E.DATA_E_HORA, E.LATITUDE, E.LONGTITUDE, E.TIPO
    FROM EVENTO E 
    WHERE E.ORGANIZADOR = <CPF>

-- 11) Listar os guardas de cada evento que criou

    SELECT P.NOME AS GUARDA, C.STATUS
    FROM CONTRATADO C JOIN PESSOA P
    ON (C.EVENTO = <ID_EVENTO> AND C.GUARDA = P.CPF)

-- 11) Postar sobre uma ocorrencia

-- 12) Listar ocorrencia pela data

    SELECT O.LONGITUDE, O.LATITUDE, O.DESCRICAO
    FROM OCORRENCIA O
    WHERE O.DATA_E_HORA = <DATA>

-- 13) Listar ocorrencia pelo local atual

    SELECT O.ID, O.DATA_E_HORA, O.TIPO, O.SUBTIPO, O.DESCRICAO
    FROM OCORRENCIA O
    WHERE O.LATITUDE = <LATITUDE> AND O.LONGITUDE = <LONGITUDE>

-- 14) Listar ocorrencia pelo Tipo e subtipo

    SELECT O.ID, O.DATA_E_HORA, O.LONGITUDE, O.LATITUDE, O.DESCRICAO
    FROM OCORRENCIA O
    WHERE O.TIPO = <TIPO> AND O.SUBTIPO = <SUBTIPO>

-- 15) Postar sobre Ponto estratégico
    
-- 16) Listar Pontos estratégicos mais proximo

    SELECT PE.NOME, PE.DESCRICAO,
    SQRT(POWER((PE.LONGITUDE - <LONGITUDE>),2) + POWER((PE.LATITUDE - <LATITUDE>),2)) AS DISTANCIA --Distância euclidiana
    FROM PONTO_ESTRATEGICO PE
    ORDER BY DISTANCIA
    
-- 18) Comentar em uma postagem especifica

-- 19) listar todos os comentarios de uma postagem (EM ORDEM)

    SELECT C.PESSOA, C.MENSAGEM
    FROM COMENTARIO JOIN POST
    ON (C.POST = P.ID)
    ORDER BY C.DATA_E_HORA

-- 20) Seguir usuários

    INSERT INTO SEGUIDOR
    (SEGUIDO, SEGUIDOR)
    VALUES <CPF_SEGUIDO> <CPF_SEGUIDOR> 

-- 21) Contratar guarda

-- 22) Organizadores com uma nota superior que a média

    SELECT P.NOME, O.NOTA
    FROM ORGANIZADOR O, PESSOA P
    WHERE O.CPF = P.CPF AND O.NOTA > (SELECT AVG(O.NOTA) FROM ORGANIZADOR O)

-- 23) Organizadores e seus ventos com uma nota superior que a média

    SELECT P.NOME AS ORGANIZADOR, O.NOTA AS NOTA_ORGANIZADOR, E.NOME AS EVENTO, E.DATA_E_HORA, E.LATITUDE, E.LONGITUDE
    FROM ORGANIZADOR O, PESSOA P, EVENTO E
    WHERE O.CPF = P.CPF AND O.CPF = E.ORGANIZADOR AND O.NOTA > (SELECT AVG(O.NOTA) FROM ORGANIZADOR O) AND E.NOTA > (SELECT AVG(E.NOTA) FROM EVENTO E)

-- VER POST DAS PESSOAS QUE ELE SEGUE


-- Pegar todas informacoes de uma determinada ocorrencia