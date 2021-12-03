class Login:
    def __init__(self,cursor):
        self.cursor = cursor
        self.loop()
    
        
    def loop():
        while(True):
            print("1 - Entrar como usuario comum")
            print("2 - Entrar como organizador")
            print("3 - Entrar como guarda")
            print("0 - Sair do programa")
            opcao = input("Entre com sua opcao:")
            print("")

            if(opcao == '1'):
                print("-----Iniciando a armazenagem de material-----")
                print("")

                peso = -1
                try:
                    resposta = requests.get( "http://127.0.0.1:5000" )
                    peso = resposta.json()["peso"]
                except:
                    print("Problema na pesagem!")#Checar se o balanca.py está rodando
                    print("")
                    continue
                
                if(peso > 0):
                    nome = input("Nome do produto:")
                    inserirProduto( nome, peso)
                else:
                    print("Problema na pesagem!")
                    print("")
                    continue

                print("")

                

            elif(opcao == '2'):
                print("-----Iniciando a retirada de material-----")
                print("")

                codigoDeBarars = input("Codigo de barras:")
                retirarProduto(codigoDeBarars)
                
                print("")

            elif(opcao == '3'):
                print("Iniciando o relatório:")
                print("")

                listarTabela()
                print("")

            elif(opcao == '4'):
                print("-----Finalizando o programa------")
                break
            else:
                print("Opcao invalida!")
                print("")

    def entrar(self, email, senha, atribuicao): #atribuicao: 1 - usuario comum , 2 - organizador e 3 - guarda
        
        if(atribuicao == 1):
            sql = "SELECT P.EMAIL, P.NOME FROM PESSOA P WHERE (P.EMAIL ='"+ email +"' AND P.SENHA = '"+ senha +"' ) LIMIT 1;"
            
        elif(atribuicao == 2):
            sql = "SELECT P.EMAIL, P.NOME, O.NOTA FROM PESSOA P JOIN ORGANIZADOR O ON(O.CPF = P.CPF) WHERE (P.EMAIL ='"+ email +"' AND P.SENHA = '"+ senha +"' ) LIMIT 1;"

        elif(atribuicao == 3):
            sql = "SELECT P.EMAIL, P.NOME, G.PERMISSAO FROM PESSOA P JOIN GUARDA G ON (P.CPF = G.CPF) WHERE (EMAIL ='"+ email +"' AND SENHA = '"+ senha +"' ) LIMIT 1;"
            
        else:
            print('Classe não encontrada')
        
        self.cursor.execute(sql)
        result = self.cursor.fetchone()

        return result
        
    def registrar(self, atribuicao):

        if(atribuicao == 1):
            self.cursor.execute("insert into ")



            