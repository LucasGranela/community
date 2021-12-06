from Telas.Tela import Tela,criarOpcoe
import credenciais


def mostrarPessoasSeguidas():
    print("")
    print("------------------------")
    print("Segue")
    print("------------------------")
    listaSeguidos = credenciais.usuario.listarSeguidos()
    if(listaSeguidos != None):
        for row in listaSeguidos():
            print('|', *row, sep='')
        print("------------------------")
        print("")
    else:
        print("Algo deu errado, verifique sua conexão com a internet.")
        print("Caso o problema persista, tente reiniciar o aplicativo.")
        print("------------------------")
        print("")




def mostrarSeguidores():
    print("")
    print("------------------------")
    print("Seguidores")
    print("------------------------")
    listaSeguidores = credenciais.usuario.listarSeguidores()
    if(listaSeguidores != None): 
        for row in listaSeguidores:
            print('|', *row, sep='')
        print("------------------------")
        print("")
    else:
        print("Algo deu errado, verifique sua conexão com a internet.")
        print("Caso o problema persista, tente reiniciar o aplicativo.")
        print("------------------------")
        print("")


def mostrarAmigosComuns():
    while(True):
        cpfUsuario = input("Digite o CPF do usuário desejado para ver seus amigos em comum, ou digite 0 para voltar:")
        
        if(len(cpfUsuario) != 11):
            if(cpfUsuario == '0'):
                break
            print("CPF inválido!")
            continue

        cpfUsuario = cpfUsuario.replace(" ", "")
        cpfUsuario = cpfUsuario.replace(".", "")
        cpfUsuario = cpfUsuario.replace("-", "")

        try:
            cpfUsuario = str(int(cpfUsuario))
        except:
            print("CPF inválido!")
            continue

        print("Seguidores em Comum")
        print("------------------------")
        amigosComuns = credenciais.usuario.amigosComuns(cpfUsuario)
        if(amigosComuns != None):
            for row in amigosComuns:
                print('|', *row, sep='')
            print("------------------------")
            print("")
        else:
            print("Algo deu errado, verifique sua conexão com a internet.")
            print("Caso o problema persista, tente reiniciar o aplicativo.")
            print("------------------------")
            print("")


        break

    
opcoes = [ 
    criarOpcoe('Pessoas que voce segue', mostrarPessoasSeguidas),
    criarOpcoe('Pessoas que te seguem', mostrarSeguidores),
    criarOpcoe('Amigos em comum com outro usuário', mostrarAmigosComuns)
]
back = criarOpcoe('Voltar')


social = Tela(opcoes,back)
