import mysql.connector

mydb = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '1234',
    database = 'python'
)
mycursor = mydb.cursor()

###  Variaveis ###
cidade = 'Rio de Janeiro'
IdCliente = '11'

### UPDATE tabela
print('UPDATE CLIENTE')
sql = "UPDATE cliente SET Cidade = %s WHERE  idCliente = %s"
val = (cidade, IdCliente)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, 'record(s) update')

