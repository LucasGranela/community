-- QUANTIDADES DE OCORRENCIA MAIS PERTO DO USUARIO 

SELECT O.DESCRICAO, O.DATA_E_HORA, O.LATITUDE, O.LONGITUDE, O.TIPO, O.fSdsUfdsafdsafsdafsdfdasfBasdfasfdsafsda
FROM PESSOA P, OCORRENCIA O
WHERE 


-- 23) Organizadores e seus ventos com uma nota superior que a média

SELECT P.NOME AS ORGANIZADOR, O.NOTA AS NOTA_ORGANIZADOR, E.NOME AS EVENTO, E.DATA_E_HORA, E.LATITUDE, E.LONGITUDE
FROM ORGANIZADOR O, PESSOA P, EVENTO E
WHERE O.CPF = P.CPF AND O.CPF = E.ORGANIZADOR AND O.NOTA > (SELECT AVG(O.NOTA) FROM ORGANIZADOR O) AND E.NOTA > (SELECT AVG(E.NOTA) FROM EVENTO E)
ORDER BY O.NOTA, E.NOTA

-- TODOS OS AMIGOS QUE ELE TEM EM COMUM COM OUTRO USUÁRIO

SELECT
FROM



-- TODOS OS USUÁRIOS QUE TEM EXATAMENTE OS MESMO AMIGOS QUE VC

SELECT dbo.fncCalcula_Distancia_Coordenada(-20.3135958, -40.2893737, -20.3480338, -40.2975204)