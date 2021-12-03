import cx_Oracle
from Controllers import usuarioController
from Views import fim,login,usuarioView



connection = cx_Oracle.connect('P11234328', 'P11234328', cx_Oracle.makedsn('grad.icmc.usp.br',15215,'orcl')) 
cursor = connection.cursor()

global usuario
usuario = None

while(True):
    opcao = login.main()

    if(opcao == '1'):

        [email, senha] = login.login()
        usuario = usuarioController.init(cursor,email,senha)
        
        if(usuario == None):
            login.invalido()
            continue
        
        login.bemSucedido()

        opcao = usuarioView.main()

        if(opcao == '1'):
        
        elif(opcao == '2'):

        elif(opcao == '3'):
        
        elif(opcao == '4'):

        elif(opcao == '0'):
        
        else:

            
        

    elif(opcao == '2'):
        print("2")

    elif(opcao == '3'):
        print("3")

    elif(opcao == '0'):
        break
    else:
        print("Opcao invalida!")
        print("")

fim.show()


cursor.close()
connection.close()
