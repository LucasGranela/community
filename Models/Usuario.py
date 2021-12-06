import BD

class Usuario:
    def __init__(self,email,senha):

        result = None
        try:
            sql = "SELECT P.CPF, P.EMAIL, P.NOME FROM PESSOA P WHERE P.EMAIL ='"+ email +"' AND P.SENHA = '"+ senha +"' "

            BD.cursor.execute(sql)
            result = BD.cursor.fetchone()
        except:
            raise Exception("Erro na inicializacao do usuario! Esse erro pode acontecer por prolemas de conexão. Tente mais tarde...")
        if(result == None):
            raise Exception("Usuário e/ou senha inválidos!")
        else:
            self.cpf = result[0]
            self.email = result[1]
            self.nome = result[2]
            self.position = [-22.00354040240801,-47.898874610042895]

        
    
    def getPosition(self):
        return self.position

    def toArray(self): 
        return {
            'CPF': self.cpf,
            'email': self.email,
            'nome': self.nome
        }

    def listarSeguidores(self):
        try:
            sql = "SELECT  P.CPF, P.NOME  FROM SEGUIDOR S JOIN PESSOA P ON S.SEGUIDOR = P.CPF WHERE S.SEGUIDO = :idUsuario"
            BD.cursor.execute(sql,[self.cpf])
            result = BD.cursor.fetchmany()

            seguidores = []

            for seguidor in result:
                seguidores.append(seguidor[1])

            return seguidores
        except:
            return None

    def listarSeguidos(self):
        try:
            sql = "SELECT  P.CPF, P.NOME  FROM SEGUIDOR S JOIN PESSOA P ON S.SEGUIDO = P.CPF WHERE S.SEGUIDOR = :idUsuario"
            BD.cursor.execute(sql,[self.cpf])
            result = BD.cursor.fetchmany()

            seguidos = []

            for segue in result:
                seguidos.append(segue[1])

            return seguidos
        except:
            return None

    def amigosComuns(self, cpfUsuario):
        try:
            sql = ('SELECT P.NOME, P.CPF FROM PESSOA P '
                'WHERE EXISTS '
                '((SELECT S.SEGUIDOR FROM SEGUIDOR S WHERE S.SEGUIDO = :CPF AND P.CPF = S.SEGUIDOR) '
                'INTERSECT '
                '(SELECT S.SEGUIDOR FROM  SEGUIDOR S WHERE S.SEGUIDO = :cpfUsuarioInteresse AND P.CPF = S.SEGUIDOR)) '
                'ORDER BY P.NOME')

            BD.cursor.execute(sql,[self.cpf, cpfUsuario])
            result = BD.cursor.fetchmany()

            amigosComuns = []

            for amigos in result:
                amigosComuns.append(amigos[0])

            return amigosComuns
        except:
            return None