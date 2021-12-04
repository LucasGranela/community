from Telas.Tela import Tela,criarOpcoe
from Controllers import usuarioController
from Telas.Ocorrencias.minhasOcorrencias import criarTelaMinhasOcorrencias
import credenciais

def mostrarOcorrenciasProximas():
    from Telas.Ocorrencias.ocorrenciasProximas import ocorrenciasProximas

    ocorrenciasProximas.show()

def mostrarMinhasOcorrencias():
    reloadMinhasOcorrencias = [True]

    while(reloadMinhasOcorrencias[0]):
        reloadMinhasOcorrencias[0] = False
        minhasOcorrencias = criarTelaMinhasOcorrencias(reloadMinhasOcorrencias) 
        minhasOcorrencias.show()

def criarOcorrencia():
    print("teste")


    

opcoes = [ 
    criarOpcoe('Ver ocorrencias proximas', mostrarOcorrenciasProximas), 
    criarOpcoe('Minhas ocorrencias',mostrarMinhasOcorrencias),
    criarOpcoe('Criar ocorrencia',criarOcorrencia),
    ]
back = criarOpcoe('Voltar')


menuOcorrencia = Tela(opcoes,back)