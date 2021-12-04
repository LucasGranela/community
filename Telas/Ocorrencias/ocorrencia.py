from Telas.Tela import Tela,criarOpcoe

def criarTelaDeOcorrencia(ocorrencia):
    
    textoComeco = ocorrencia.getFormatada()

    opcoes =[
        criarOpcoe("Deletar"),
        criarOpcoe("Editar")
    ]
    back = criarOpcoe('Voltar')

    ocorrenciasProximas = Tela(opcoes,back,textoComeco)
    return ocorrencia