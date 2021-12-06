import cx_Oracle

connection = None
cursor = None

print("")
print("Tentando conectar ao banco de dados....")
print("")
try:
    connection = cx_Oracle.connect('P11234328', 'P11234328', cx_Oracle.makedsn('grad.icmc.usp.br',15215,'orcl')) 
    cursor = connection.cursor()
except:
    print("Nao foi possivel conectar com o banco de dados!")