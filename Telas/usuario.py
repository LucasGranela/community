from Telas.Tela import Tela,criarOpcoe
from Telas.social import social
from Telas.Ocorrencias.menuOcorrencia import menuOcorrencia
from Controllers import usuarioController

def mostrarOcorrencia():
    menuOcorrencia.show()
    

def mostrarSocial():
    social.show()

    

opcoes = [ criarOpcoe('Ocorrencias', mostrarOcorrencia), criarOpcoe('Social', mostrarSocial) ]
back = criarOpcoe('Logout')


telaUsuario = Tela(opcoes,back)