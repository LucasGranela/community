import BD

class Ocorrencia:
    def __init__(self,ID, dataEHora, latitude, longitude, tipo, subtipo, estado, descricao = None, criador = None):

        self.ID = ID
        self.dataEHora = dataEHora
        self.latitude = latitude
        self.longitude = longitude
        self.tipo = tipo
        self.subtipo = subtipo
        self.estado = estado
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
        return  self.tipo + ": " + self.subtipo + " - " + str(self.dataEHora)
    
    def getFormatada(self):
        ocorrenciaTxt = self.tipo + ": " + self.subtipo + " - " + str(self.dataEHora) + "\n"
        # ocorrenciaTxt += "Criador: "  + self.criador + "\n"
        ocorrenciaTxt += "Latitude: " + str(self.latitude) + "   Longitude: " + str(self.longitude) + "\n"
        ocorrenciaTxt += "Estado: " + self.estado + "\n"
        ocorrenciaTxt += "Descricao: "  + self.descricao + "\n"
        
        for post in self.posts:
            ocorrenciaTxt += post.getFormatada

        return ocorrenciaTxt
    
    def loadPosts(self):
        self.posts = []

    @staticmethod
    def getOcorrenciasRegiao(latitude,longitude):
        result=[
            [1, "05/06/2001", "1111", "2222", "Estrutural", "Alagamento","Nao verificado"],
            [2, "05/06/2001", "1111", "2222", "Estrutural", "Incendio","Nao verificado"],
            [3, "05/06/2001", "1111", "2222", "Estrutural", "Cano quebrado","Nao verificado"]
        ]

        ocorrencias = []

        for ocorrencia in result:
            ocorrencias.append(Ocorrencia(*ocorrencia))

        return ocorrencias
    
    @staticmethod
    def getOcorrenciaDeUmUsuario(idUsuario):
        result=[
            [1, "05/06/2001", "1111", "2222", "Estrutural", "Alagamento","Nao verificado"],
            [2, "05/06/2001", "1111", "2222", "Estrutural", "Incendio","Nao verificado"],
            [3, "05/06/2001", "1111", "2222", "Estrutural", "Cano quebrado","Nao verificado"]
        ]

        ocorrencias = []

        for ocorrencia in result:
            ocorrencias.append(Ocorrencia(*ocorrencia))

        return ocorrencias


        
