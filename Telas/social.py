from Telas.Tela import Tela,criarOpcoe

def interacoesDosSeguidores():
    print("teste")

def mostrarPessoasSeguidas():
    print("teste")

def mostrarSeguidores():
    print("teste")

    

opcoes = [ 
    criarOpcoe('Ver interacoes com pessoas que voce segue',interacoesDosSeguidores),
    criarOpcoe('Pessoas que voce segue', mostrarPessoasSeguidas),
    criarOpcoe('Pessoas que te seguem', mostrarSeguidores)
]
back = criarOpcoe('Voltar')


social = Tela(opcoes,back)
