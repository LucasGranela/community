from Views import login 
from Controllers import usuarioController

def loopPrincipal(cursor):
     while(True):
            opcao = login.main()

            if(opcao == '1'):

                [email, senha] = login.login()
                usuarioController.init(cursor,email,senha)
                break

            elif(opcao == '2'):
                print("2")

            elif(opcao == '3'):
                print("3")

            elif(opcao == '0'):
                break
            else:
                print("Opcao invalida!")
                print("")