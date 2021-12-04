from Telas.Tela import Tela,criarOpcoe
from Controllers import usuarioController
import credenciais

def mostrarOcorrenciasProximas():
    print("teste")

def mostrarMinhasOcorrencias():
    print("teste")

def criarOcorrencia():
    print("teste")


    

opcoes = [ 
    criarOpcoe('Ver ocorrencias proximas', mostrarOcorrenciasProximas), 
    criarOpcoe('Minhas ocorrencias',mostrarMinhasOcorrencias),
    criarOpcoe('Criar ocorrencia',criarOcorrencia),
    ]
back = criarOpcoe('Voltar')


menuOcorrencia = Tela(opcoes,back)