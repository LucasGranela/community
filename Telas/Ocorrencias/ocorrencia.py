from Telas.Tela import Tela,criarOpcoe
from opcoes import tiposOcorrencia,subtiposOcorrenciaCriminal,subtiposOcorrenciaCriminalValues,subtiposOcorrenciaEstrutural,subtiposOcorrenciaEstruturalValues,terminalSelect

def criarTelaDeOcorrencia(ocorrencia, eCriador = False):

    def deletar():
        if(ocorrencia.delete()):
            print("Ocorrencia deletada com sucesso!")
        else:
            print("Por algum motivo nao foi possivel deletar essa ocorrencia!")
            print("Verifique sua conexao com a internt.")
            print("Caso o problema persista, tente reiniciar o programa.")



    def editar():
        latitude = None
        while(True):
            try:
                latitude = input("Latitude: ")

                if(latitude == "" or latitude == None):
                    break
                else:
                    latitude = str(float(latitude))
                    break
            except:
                print("Latitude invalida.")
                continue
        longitude = None
        while(True):
            try:
                longitude = input("Longitude: ")

                if(longitude == "" or longitude == None):
                    break
                else:
                    longitude = str(float(longitude))
                    break
            except:
                print("Longitude invalida.")
                continue
        
        print('----Tipo----')

        tipo = terminalSelect(tiposOcorrencia,None,True)
        if(tipo =="" or tipo == None):
            tipo = int(ocorrencia.toArray()['tipo'])

        subtipo =""

        print('----Subtipo----')
        if(tipo == 0):
            subtipo = terminalSelect(subtiposOcorrenciaCriminal,subtiposOcorrenciaCriminalValues,True)
        if(tipo == 1):
            subtipo = terminalSelect(subtiposOcorrenciaEstrutural,subtiposOcorrenciaEstruturalValues,True)
        
        descricao = input("Descricao: ")
        
        if(ocorrencia.edite(latitude,longitude,tipo,subtipo,descricao)):
            print("Ocorrencia editada com sucesso!")
        else:
            print("Algo deu errado na edicao da ocorrencia! Verifique sua conexao com a internet.")
            print("Se o problema persistir, tente reiniciar o programa.")

            

    
    textoComeco = ocorrencia.getFormatada()

    opcoes = []
    if(eCriador):
        opcoes =[
            criarOpcoe("Deletar",deletar),
            criarOpcoe("Editar",editar)
        ]
    
    back = criarOpcoe('Voltar')

    telaOcorrencia = Tela(opcoes,back,textoComeco,ocorrencia.getPrecisaAtualizar)
    return telaOcorrencia