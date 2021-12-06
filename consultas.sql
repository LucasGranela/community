-- 1) Organizadores e seus ventos com uma nota superior que a média (TESTAR PARA VERIFICAR MELHOR QUANDO A BASE ESTIVER MAIOR)

SELECT P.NOME AS ORGANIZADOR, O.NOTA AS NOTA_ORGANIZADOR, E.NOME AS EVENTO,
       E.NOTA AS NOTA_EVENTO, E.DATA_E_HORA, E.LATITUDE, E.LONGITUDE
FROM PESSOA P JOIN ORGANIZADOR O ON P.CPF = O.CPF AND O.NOTA > (SELECT AVG(O.NOTA) FROM ORGANIZADOR O) 
JOIN EVENTO E ON  O.CPF = E.ORGANIZADOR AND E.NOTA > (SELECT AVG(E.NOTA) FROM EVENTO E)
ORDER BY O.NOTA, E.NOTA;

-- 2) CONSULTAR SEGUIDORES COMUNS ENTRE DOIS USUÁRIOS

SELECT P.NOME, P.CPF
FROM PESSOA P
WHERE EXISTS
    ((SELECT S.SEGUIDOR FROM SEGUIDOR S WHERE S.SEGUIDO = '56153503650' AND P.CPF = S.SEGUIDOR)
    INTERSECT
    (SELECT S.SEGUIDOR FROM  SEGUIDOR S WHERE S.SEGUIDO = '89200907806' AND P.CPF = S.SEGUIDOR)
    )
ORDER BY P.NOME;


-- 3) CONSULTAR O NÚMERO DE SEGUIDORES DE UM USUÁRIO QUE IRÃO AOS EVENTOS

SELECT E.NOME, COUNT(S.SEGUIDOR) AS NUMERO_DE_SEGUIDORES
FROM SEGUIDOR S JOIN PARTICIPANTE PA ON PA.PESSOA = S.SEGUIDOR AND S.SEGUIDO = '56153503650'
RIGHT JOIN EVENTO E ON PA.EVENTO = E.ID 
GROUP BY E.ID,E.NOME
ORDER BY E.NOME;

-- 4) QUANTIDADE DE COMENTÁRIOS NOS POST DAS OCORRÊNCIAS (TOP 20)

SELECT * FROM 
(SELECT PT.ID, P1.NOME AS CRIADOR_POST, PT.MENSAGEM AS POST, COUNT(C.ID) AS NUM_COMENTARIOS 
FROM OCORRENCIA O 
JOIN POST_OCORRENCIA PO ON O.ID = PO.OCORRENCIA
JOIN POST PT ON PT.ID = PO.POST
JOIN PESSOA P1 ON PT.PESSOA = P1.CPF
LEFT JOIN COMENTARIO C ON PT.ID = C.POST
GROUP BY PT.ID, P1.NOME, PT.MENSAGEM
ORDER BY NUM_COMENTARIOS DESC)
WHERE ROWNUM <= 2;

-- 5) PESSOA QUE FORAM/VÃO AOS MESMO EVENTOS QUE UM DETERMINADO USUÁRIO

SELECT P.NOME FROM PESSOA P 
WHERE NOT EXISTS (
    (SELECT PA.EVENTO FROM PARTICIPANTE PA WHERE PA.PESSOA = '62174394125')
    MINUS
    (SELECT PA.EVENTO FROM PARTICIPANTE PA WHERE PA.PESSOA = P.CPF AND PA.PESSOA <> '62174394125')
)

-- 6) GUARDA VISUALIZAR TODAS AS OCORRÊNCIA DO TIPO CRIMINAL E OS POSTS RELACIONADOS, EM UM EVENTO QUE ELE ESTÁ TRABALHANDO

SELECT O.ID AS ID_OCORRENCIA, P1.NOME AS CRIADOR_OCORRENCIA, O.DESCRICAO, PT.ID AS ID_POST, 
       P2.NOME AS CRIADOR_POST, PT.MENSAGEM AS POST, C.ID AS ID_COMENTARIO, 
       P3.NOME AS PESSOA_COMENTOU, C.MENSAGEM AS COMENTARIO
FROM CONTRATADO C JOIN CRIMINAL CR ON C.EVENTO = CR.IDEVENTO
JOIN OCORRENCIA O ON O.ID = CR.ID
JOIN PESSOA P1 ON O.CRIADOR = P1.CPF
LEFT JOIN POST_OCORRENCIA PO ON PO.OCORRENCIA = O.ID
LEFT JOIN POST PT ON PT.ID = PO.POST
LEFT JOIN PESSOA P2 ON PT.PESSOA = P2.CPF
LEFT JOIN COMENTARIO C ON C.POST = PT.ID
LEFT JOIN PESSOA P3 ON C.PESSOA = P3.CPF
WHERE C.GUARDA = '60932730348' AND C.EVENTO = 1 AND C.STATUS = 1

-- 7) PROCURAR POSTS DE OCORRÊNCIAS CRIMINAIS RELACIONADAS A UM DETERMINADO EVENTO POR PALAVRA CHAVE

SELECT PT.ID AS ID_POST, P.NOME AS CRIADOR_POST, PT.MENSAGEM AS POST
FROM CRIMINAL C JOIN OCORRENCIA O ON C.ID = O.ID
JOIN POST_OCORRENCIA PO ON PO.OCORRENCIA = O.ID
JOIN POST PT ON PT.ID = PO.POST AND PT.MENSAGEM LIKE '%ROUBO%'
JOIN PESSOA P ON PT.PESSOA = P.CPF
WHERE C.IDEVENTO = 1;

-- EXTRAS:

-- OCORRENCIA MAIS PRÓXIMAS AO USUÁRIO 

SELECT  O.ID, 
        O.DATA_E_HORA, 
        O.LATITUDE, 
        O.LONGITUDE, 
        O.TIPO, 
        O.SUBTIPO, 
        O.ESTADO, 
        O.DESCRICAO,
        O.CRIADOR,
        CDLL(O.LATITUDE, O.LONGITUDE, <LAGITUDE_PESSOA>, <LONGITUDE_PESSOA>) AS DISTANCIA 
FROM  OCORRENCIA O 
WHERE CDLL(O.LATITUDE, O.LONGITUDE, <LAGITUDE_PESSOA>, <LONGITUDE_PESSOA>) <= < DISTANCIA_MAXIMA>
ORDER BY DISTANCIA

-- SELECIONAR TODOS OS SEUS SEGUIDORES QUE PARTICIPAM DE UM DETERMINADO EVENTO 

SELECT P.NOME
FROM PESSOA P JOIN SEGUIDOR S
ON S.SEGUIDO = '89200907806' AND P.CPF = S.SEGUIDOR
JOIN PARTICIPANTE PA
ON PA.PESSOA = S.SEGUIDOR AND PA.EVENTO = 0
ORDER BY PA.EVENTO;