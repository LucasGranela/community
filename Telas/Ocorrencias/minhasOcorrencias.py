from Telas.Tela import Tela,criarOpcoe
import credenciais
from Models.Ocorrencia import Ocorrencia

ocorrencias = []

print(credenciais.usuario)

if(credenciais.usuario != 0):
    ocorrencias = Ocorrencia.getOcorrenciaDeUmUsuario(credenciais.usuario.toArray()["CPF"])

def createMostrarOcorrencia(indexOcorrencia):
    
    def mostrarOcorrencia():
        print(str(indexOcorrencia))
    
    return mostrarOcorrencia
    
textoComeco = "Escolha uma ocorrência ou digite 0 para voltar"
opcoes = []

count = 0
for ocorrencia in ocorrencias:
    opcoes.append(criarOpcoe(ocorrencia.printResumo(),createMostrarOcorrencia(count)))

back = criarOpcoe('Voltar')


minhasOcorrencias = Tela(opcoes,back,textoComeco)