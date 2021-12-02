import cx_Oracle

connection = cx_Oracle.connect(user="P11234328", password="P11234328",
                               dsn="grad.icmc.usp.br:1984/orcl",
                               encoding="UTF-8")

print(connection.version)