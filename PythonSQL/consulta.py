import mysql.connector


mydb = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '1234',
    database = 'python'
)

mycursor = mydb.cursor()

### consulta tabela
print('CONSULTAR CLIENTE')
mycursor.execute('SELECT * FROM cliente')
myresult = mycursor.fetchall()

for line in myresult:
    print ('line: ', line)
    