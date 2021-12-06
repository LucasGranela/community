from Telas.Tela import Tela,criarOpcoe
from Telas.Ocorrencias.ocorrencia import criarTelaDeOcorrencia
from Models.Ocorrencia import Ocorrencia
import credenciais

def criarTelaOcorrenciasProximas():

    def createMostrarOcorrencia(indexOcorrencia):
        
        def mostrarOcorrencia():
            telaOcorrencia = criarTelaDeOcorrencia(credenciais.ocorrencias[indexOcorrencia])
            telaOcorrencia.show()
        
        return mostrarOcorrencia

    if(credenciais.usuario != None):
            credenciais.ocorrencias = Ocorrencia.getOcorrenciasRegiao(*credenciais.usuario.getPosition())
        
    textoComeco = "Escolha uma ocorrência ou digite 0 para voltar"
    opcoes = []

    count = 0
    if(credenciais.ocorrencias != None):
        for ocorrencia in credenciais.ocorrencias:
            if(ocorrencia != None):
                opcoes.append(criarOpcoe(ocorrencia.getResumo(),createMostrarOcorrencia(count)))
            count +=1
    elif(credenciais.ocorrencias == []):
        print('Nao foram encontradas ocorrencias.')
    else:
        print("Houve alguma erro no carregamento. Verifique sua conexao de internet!")
        
    back = criarOpcoe('Voltar')


    ocorrenciasProximas = Tela(opcoes,back,textoComeco)

    return ocorrenciasProximas