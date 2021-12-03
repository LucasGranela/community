import cx_Oracle
from Controllers import init
from Views import fim

global usuario

connection = cx_Oracle.connect('P11234328', 'P11234328', cx_Oracle.makedsn('grad.icmc.usp.br',15215,'orcl')) 
cursor = connection.cursor()

init.loopPrincipal(cursor)

fim.show()

print(usuario.toArray())

cursor.close()
connection.close()
