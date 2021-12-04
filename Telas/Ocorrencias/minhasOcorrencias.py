from Telas.Tela import Tela,criarOpcoe
from Telas.Ocorrencias.ocorrencia import criarTelaDeOcorrencia
from Models.Ocorrencia import Ocorrencia
import credenciais

def createMostrarOcorrencia(indexOcorrencia):
    
    def mostrarOcorrencia():
        ocorrencia = criarTelaDeOcorrencia(credenciais.ocorrencias[indexOcorrencia])
        ocorrencia.show()
    
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


minhasOcorrencias = Tela(opcoes,back,textoComeco)