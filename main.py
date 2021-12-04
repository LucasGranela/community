import credenciais
import BD
from Telas.inicio import inicio

inicio.show()

BD.cursor.close()
BD.connection.close()

