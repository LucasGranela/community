from Models.Ocorrencia import Ocorrencia
from Telas.Tela import Tela,criarOpcoe
from Telas.Ocorrencias.minhasOcorrencias import criarTelaMinhasOcorrencias
from Telas.Ocorrencias.ocorrenciasProximas import criarTelaOcorrenciasProximas
from opcoes import tiposOcorrencia,subtiposOcorrenciaCriminal,subtiposOcorrenciaCriminalValues,subtiposOcorrenciaEstrutural,subtiposOcorrenciaEstruturalValues,terminalSelect
import credenciais

def mostrarOcorrenciasProximas():
    ocorrenciasProximas = criarTelaOcorrenciasProximas()
    ocorrenciasProximas.show()

def mostrarMinhasOcorrencias():
    reloadMinhasOcorrencias = [True]

    while(reloadMinhasOcorrencias[0]):
        reloadMinhasOcorrencias[0] = False
        minhasOcorrencias = criarTelaMinhasOcorrencias(reloadMinhasOcorrencias) 
        minhasOcorrencias.show()

def criarOcorrencia():
   
    latitude = None
    while(True):
        try:
            latitude = input("Latitude: ")
            latitude = str(float(latitude))

            break
        except:
            print("Latitude invalida.")
            continue
    longitude = None
    while(True):
        try:
            longitude = input("Longitude: ")
            longitude = str(float(longitude))
            
            break

        except:
            print("Longitude invalida.")
            continue
    
    
    print('----Tipo----')
    tipo = terminalSelect(tiposOcorrencia,None,False)
    print('----Subtipo----')
    if(tipo == 0):
        subtipo = terminalSelect(subtiposOcorrenciaCriminal,subtiposOcorrenciaCriminalValues,False)
    if(tipo == 1):
        subtipo = terminalSelect(subtiposOcorrenciaEstrutural,subtiposOcorrenciaEstruturalValues,False)
    descricao = input("Descricao: ")
    
    if(Ocorrencia.criar(latitude,longitude,tipo,subtipo,descricao,credenciais.usuario.toArray()["CPF"])):
        print("Ocorrencia criada com sucesso!")
    else:
        print("Algo deu errado na criacao da ocorrencia! Verifique sua conexao com a internet.")
        print("Se o problema persistir, tente reiniciar o programa.")



    

opcoes = [ 
    criarOpcoe('Ver ocorrencias proximas', mostrarOcorrenciasProximas), 
    criarOpcoe('Minhas ocorrencias',mostrarMinhasOcorrencias),
    criarOpcoe('Criar ocorrencia',criarOcorrencia),
    ]
back = criarOpcoe('Voltar')


menuOcorrencia = Tela(opcoes,back)