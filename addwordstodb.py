import psycopg2 as pc
import dbconfig as dbc

conn = pc.connect(database =dbc.database, user = dbc.user, password=dbc.password, host=dbc.host, port=dbc.port)
conn.autocommit = True
cursor = conn.cursor()
with open("slowa.csv", "r", encoding="utf-8") as f:
    f.readline()
    i = 1
    while True:
        buff = f.readline()[:-1].split(",")
        cursor.execute(
            'INSERT INTO WORDS(pol, de, set) VALUES (%s,%s,%s)',(buff[1],buff[0],(i/100+1) )
                       )
        i+=1
        if not buff:
            break