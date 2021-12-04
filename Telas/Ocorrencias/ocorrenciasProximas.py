from Telas.Tela import Tela,criarOpcoe
from Models.Ocorrencia import Ocorrencia
import credenciais

def createMostrarOcorrencia(indexOcorrencia):
    
    def mostrarOcorrencia():
        print(str(indexOcorrencia))
    
    return mostrarOcorrencia

if(credenciais.usuario != None):
        credenciais.ocorrencias = Ocorrencia.getOcorrenciaDeUmUsuario(credenciais.usuario.toArray()["CPF"])
    
textoComeco = "Escolha uma ocorrência ou digite 0 para voltar"
opcoes = []

count = 0
for ocorrencia in credenciais.ocorrencias:
    opcoes.append(criarOpcoe(ocorrencia.getResumo(),createMostrarOcorrencia(count)))
    count +=1

back = criarOpcoe('Voltar')


ocorrenciasProximas = Tela(opcoes,back,textoComeco)