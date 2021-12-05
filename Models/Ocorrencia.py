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
        self.precisaAtualizar = False
        
        
    
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
        return  str(self.tipo) + ": " + str(self.subtipo) + " - " + str(self.dataEHora)
    


    def getFormatada(self):
        ocorrenciaTxt = str(self.tipo) + ": " + str(self.subtipo) + " - " + str(self.dataEHora) + "\n"
        # ocorrenciaTxt += "Criador: "  + self.criador + "\n"
        ocorrenciaTxt += "Latitude: " + str(self.latitude) + "   Longitude: " + str(self.longitude) + "\n"
        ocorrenciaTxt += "Estado: " + str(self.estado) + "\n"
        ocorrenciaTxt += "Descricao: "  + str(self.descricao) + "\n"
        
        for post in self.posts:
            ocorrenciaTxt += post.getFormatada

        return ocorrenciaTxt
    


    def loadPosts(self):
        self.posts = []



    def delete(self):
        try:
            sql = 'DELETE FROM OCORRENCIA WHERE ID = :ID'
            BD.cursor.execute(sql,[self.ID])
            BD.connection.commit()
            self.precisaAtualizar = True
            return True
        except:
            return False

        

    def getPrecisaAtualizar(self):
        return self.precisaAtualizar



    def edite(self,latitude,longitude,tipo,subtipo,descricao):
        # try:
            if(latitude != None and latitude != ""):
                self.latitude = latitude
            if(longitude != None and longitude != ""):
                self.longitude = longitude
            if(tipo != None and tipo != ""):
                self.tipo = tipo
            if(subtipo != None and subtipo != ""):
                self.subtipo = subtipo
            if(descricao != None and descricao != ""):
                self.descricao = descricao

            sql = 'UPDATE OCORRENCIA SET LATITUDE = :LATITUDE, LONGITUDE = :LONGITUDE, TIPO = :TIPO , SUBTIPO = :SUBTIPO , DESCRICAO = :DESCRICAO WHERE ID= :ID'
            BD.cursor.execute(sql,[self.latitude,self.longitude,self.tipo,self.subtipo,self.descricao,self.ID])
            BD.connection.commit()

            self.precisaAtualizar = True

            return True
        # except:
            return False
        


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
        sql = "SELECT ID, DATA_E_HORA, LATITUDE, LONGITUDE, TIPO, SUBTIPO, ESTADO, DESCRICAO, CRIADOR FROM OCORRENCIA WHERE CRIADOR = :idUsuario"
        BD.cursor.execute(sql,[idUsuario])
        result = BD.cursor.fetchmany()

        ocorrencias = []

        for ocorrencia in result:
            ocorrencias.append(Ocorrencia(*ocorrencia))

        return ocorrencias


        
