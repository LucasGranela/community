import BD

class Ocorrencia:
    def __init__(self,ID, dataEHora, latitude, longitude, tipo, subtipo, Estado, descricao = None, criador = None):

        self.ID = ID
        self.dataEHora = dataEHora
        self.latitude = latitude
        self.longitude = longitude
        self.tipo = tipo
        self.subtipo = subtipo
        self.descricao = descricao
        self.criador = criador
        self.posts = []
        
        
    
    def toArray(self): 
        return {
            'ID': self.ID,
            'dataEHora': self.dataEHora,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'tipo': self.tipo,
            'subtipo': self.subtipo,
            'descricao': self.descricao,
            'criador': self.criador
        }

    def getResumo(self): 
        return  self.tipo + ": " + self.subtipo + " - " + str(dataEHora)
    
    def getPosts(self):
        self.posts = []

    @staticmethod
    def getOcorrenciasRegiao(latitude,longitude):
        print('getOcorrenciasRegiao')
    
    @staticmethod
    def getOcorrenciaDeUmUsuario(idUsuario):
        result=[
            [1, "05/06/2001", "1111", "2222", "Estrutural", "Carro quebrado"],
            [2, "05/06/2001", "1111", "2222", "Estrutural", "Carro quebrado"],
            [3, "05/06/2001", "1111", "2222", "Estrutural", "Carro quebrado"]
        ]

        ocorrencias = []

        for ocorrencia in result:
            ocorrencias.append(Ocorrencia(*ocorrencia))

        return ocorrencias


        
