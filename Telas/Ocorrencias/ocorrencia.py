from Telas.Tela import Tela,criarOpcoe

def criarTelaDeOcorrencia(ocorrencia):

    def deletar():
        ocorrencia.delete()

    def editar():
        latitude = input("Latitude: ")
        longitude = input("Longitude: ")
        tipo = input("Tipo: ")
        subtipo =  input("Subtipo: ")
        descricao = input("Descricao: ")
        ocorrencia.edite(latitude,longitude,tipo,subtipo,descricao)
    
    textoComeco = ocorrencia.getFormatada()

    opcoes =[
        criarOpcoe("Deletar",deletar),
        criarOpcoe("Editar",editar)
    ]
    back = criarOpcoe('Voltar')

    telaOcorrencia = Tela(opcoes,back,textoComeco,ocorrencia.getPrecisaAtualizar)
    return telaOcorrencia