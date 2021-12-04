from Telas.Tela import Tela,criarOpcoe
from Telas.Ocorrencias.minhasOcorrencias import minhasOcorrencias
from Controllers import usuarioController
import credenciais

def mostrarOcorrenciasProximas():
    print("teste")

def mostrarMinhasOcorrencias():
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