from Telas.Tela import Tela,criarOpcoe
from Telas.usuario import telaUsuario
from Controllers import usuarioController
import credenciais


def login():
    print("")
    
    email = input("Email: ")
    senha = input("Senha: ")

    credenciais.usuario = usuarioController.init(email, senha)

    print(credenciais.usuario)

    if(credenciais.usuario != None):
        telaUsuario.show()


    

opcoes = [ criarOpcoe('Entrar como usuario comum',login) ]
back = criarOpcoe('Fechar programa')


inicio = Tela(opcoes,back)
