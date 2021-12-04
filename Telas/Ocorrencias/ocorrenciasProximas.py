from Telas.Tela import Tela,criarOpcoe
import credenciais

ocorrencias = []

def createMostrarOcorrencia(indexOcorrencia):
    
    def mostrarOcorrencia():
        print(str(indexOcorrencia]))
    
    return mostrarOcorrencia
    
textoComeco = "Escolha uma ocorrência ou digite 0 para voltar"
opcoes = []

count = 0
for ocorrencia in ocorrencias:
    opcoes.append(criarOpcoe(ocorrencia.getResumo(),createMostrarOcorrencia(count)))

back = criarOpcoe('Voltar')


ocorrenciasProximas = Tela(opcoes,back,textoComeco)