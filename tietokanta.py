import mysql.connector
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='root',
    password='Assi',
    autocommit=True
)

#määritelty kysely
maakoodi = input("Anna 2-kirjaiminen maakoodi")
sql = "SELECT name, continent FROM country WHERE iso_country = '" + maakoodi + "'"
print(sql)