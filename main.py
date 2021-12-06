print("------ Community ------")
import credenciais
import BD
from Telas.inicio import inicio

if(BD.connection != None and BD.cursor != None):
    
    inicio.show()

    BD.cursor.close()
    BD.connection.close()

