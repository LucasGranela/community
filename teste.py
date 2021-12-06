latitude = input("Latitude: ")
longitude = input("Longitude: ")
print('----Tipo----')
tipo = terminalSelect(tiposOcorrencia,None,True)
if(tipo =="" or tipo == None):
    tipo = int(ocorrencia.toArray()['tipo'])
print('----Subtipo----')
if(tipo == 0):
    subtipo = terminalSelect(subtiposOcorrenciaCriminal,subtiposOcorrenciaCriminalValues,True)
if(tipo == 1):
    subtipo = terminalSelect(subtiposOcorrenciaEstrutural,subtiposOcorrenciaEstruturalValues,True)
descricao = input("Descricao: ")