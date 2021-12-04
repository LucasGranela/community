from Telas.Tela import Tela,criarOpcoe
from Controllers import usuarioController
import credenciais

def mostrarOcorrenciasProximas():
    from Telas.Ocorrencias.ocorrenciasProximas import ocorrenciasProximas

    ocorrenciasProximas.show()

def mostrarMinhasOcorrencias():
    from Telas.Ocorrencias.minhasOcorrencias import minhasOcorrencias

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