import mysql.connector

mydb = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '1234',
    database = 'python'
)
mycursor = mydb.cursor()
### deletar tabela
print('DELETE CLIENTE')
sql = "DELETE FROM cliente WHERE IdCliente = '4'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, 'record(s) deleted')