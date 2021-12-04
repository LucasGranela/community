import BD

class Usuario:
    def __init__(self,email,senha):

        # result = None
        # try:
        #     sql = "SELECT P.CEP, P.EMAIL, P.NOME FROM PESSOA P WHERE P.EMAIL ='"+ email +"' AND P.SENHA = '"+ senha +"' "

        #     BD.cursor.execute(sql)
        #     result = BD.cursor.fetchone()
        # except:
        #     raise Exception("Erro na inicializacao do usuario! Esse erro pode acontecer por prolemas de conexão. Tente mais tarde...")
        # if(result == None):
        #     raise Exception("Usuário e/ou senha inválidos!")
        # else:
        #     self.cpf = result[0]
        #     self.email = result[1]
        #     self.nome = result[2]

        self.cpf = "52803356813"
        self.email = "pinto@"
        self.nome = "pinto"
    
    def toArray(self): 
        return {
            'cpf': self.cpf,
            'email': self.email,
            'nome': self.nome
        }
