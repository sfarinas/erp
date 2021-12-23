import mysql.connector

mydb = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '1234',
    database = 'python'
)
mycursor = mydb.cursor()
### UPDATE tabela
print('UPDATE CLIENTE')
sql = "INSERT INTO cliente (Nome, Telefone, Cidade) VALUES (%s, %s, %s)"
val = ('Silva', '45779631', 'Nigeria')
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, 'record(s) insert')

