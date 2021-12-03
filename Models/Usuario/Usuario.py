class Usuario:
    def __init__(self,cursor,email,senha):

        result = None
        try:
            sql = "SELECT P.EMAIL, P.NOME FROM PESSOA P WHERE P.EMAIL ='"+ email +"' AND P.SENHA = '"+ senha +"' "

            cursor.execute(sql)
            result = cursor.fetchone()
        except:
            raise Exception("Erro na inicializacao do usuario! Esse erro pode acontecer por prolemas de conexão. Tente mais tarde...")
        if(result == None):
            raise Exception("Usuário e/ou senha inválidos!")
        else:
            self.email = result[0]
            self.nome = result[1]
    
    def toArray(self): 
        return {
            'email': self.email,
            'nome': self.nome
        }
